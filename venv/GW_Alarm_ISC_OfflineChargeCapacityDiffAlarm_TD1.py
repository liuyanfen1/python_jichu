#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# copyright (c) 2022 SVOLT Energy.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the contract with SVOLT Energy.

"""
# @Time    : 2023/03/17
# @Author  : 王棚超
# @FileName: GW_Alarm_ISC_OfflineChargeCapacityDiffAlarm_TD1.py
# @Software: PyCharm
# @Version : V3.0.0  create 定阈值后首次部署20230317

"""
# name: GW_Alarm_ISC_OfflinedChargeCapacityDiffAlarm_TD1
# from: dw_gb32960_battery.d_i_svolt_battery_detail
# to: dm_battery_alarm.d_i_alarm_results
# comments: 车辆电池数据从dw层->dm层(离线充电容量偏差预警V3.0)

import sys
from pyspark.sql import SparkSession, Window, SQLContext
from pyspark.sql import functions
from pyspark.sql.types import *
import pandas as pd
import numpy as np
import json
import time
import datetime
from battery_alarm_toolkit.alarm import gen_alarm_id, gen_hash_code
from battery_alarm_toolkit.algorithm import Algorithm
from collections import defaultdict
from battery_alarm_toolkit import proxima
from matplotlib.cbook import boxplot_stats

global input_date, algorithm_id, algorithm_env, algorithm, algorithm_params_id, alarm_id

# 事件特征schema
alarmSchema = StructType([
    StructField("algorithm_id", StringType(), True),
    StructField("algorithm_params_id", StringType(), True),
    StructField("battery_id", StringType(), True),
    StructField("device_id", StringType(), True),
    StructField("process_id", StringType(), True),
    StructField("msg_type", StringType(), True),
    StructField("alarm_data", StringType(), True),
    StructField("hash_code", StringType(), True),
    StructField("result_create_time", LongType(), True),
    StructField("create_time", LongType(), True),
    StructField("update_time", LongType(), True),
    StructField("alarm_id", StringType(), True),
    StructField("data_source", StringType(), True),
    StructField("data_type", StringType(), True)
])


class NpEncoder(json.JSONEncoder):
    """
    转换numpy数据类型为python3数据类型
    """

    def default(self, obj):
        """
        数据类型转换
        :param obj: numpy 数据
        :return: Python3 数据
        """
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)


def get_battery_alarm(alarm_group):
    """
    :param alarm_group: 初步过滤出满足条件的告警数据
    :return: res: 进一步过滤出的有效告警数据
    """
    res = pd.DataFrame(
        columns=(
            "algorithm_id", "algorithm_params_id", "battery_id", "device_id", "process_id", "msg_type", "alarm_data",
            "hash_code", "result_create_time", "create_time", "update_time", "alarm_id", "data_source", "data_type"
        )
    )

    column = ["vin", "battery_id", "vehicle_type", "battery_model", "charge_order",  "sample_time", "sample_timestamp",
              "user_soc", "voltage", "current", "vehicle_insulation_resistance",
              "max_probe_temperature_sn", "max_probe_temperature", "min_probe_temperature_sn", "min_probe_temperature",
              "max_cell_voltage_sn", "max_cell_voltage", "min_cell_voltage_sn", "min_cell_voltage",
              "charge_vehicle_mileage"]

    alarm_group = pd.DataFrame(alarm_group, columns=column)
    alarm_group = alarm_group.where(alarm_group.notnull(), None)
    alarm_group = alarm_group.sort_values("sample_timestamp")
    alarm_group = alarm_group.reset_index(drop=True)

    charge_max_current = max(alarm_group["current"].values)

    window_size = 30
    std_threshold = 0.5  # 0.5mV/0.0005V

    capacity_rate_dict = {
        "CC7000ZM00GBEV": {"09UPB53EQDJ371": 104},
        "CC7000BJ02DBEV": {"09UPB45MQDYMW3": 184},
        "CC7000CG01ABEV": {"09UPB40MQEU823": 184},
        "CC7000BH02ABEV": {"09UPB63M343HY2": 184},
        "CC6470AH05GPHEV": {"0KEPB79P3NJW39": 23.2}
    }
    vehicle_type = alarm_group.loc[0, "vehicle_type"]
    battery_model = alarm_group.loc[0, "battery_model"]
    try:
        capacity_rate = capacity_rate_dict[vehicle_type][battery_model]
    except:
        print(999999999999, vehicle_type, battery_model)
        return [[None] * 14]

    max_volt_in_plat_time, max_volt_in_plat_timestamp, max_volt_out_plat_time = None, None, None
    min_volt_in_plat_time, min_volt_in_plat_timestamp, min_volt_out_plat_time = None, None, None

    max_voltage_filtered = alarm_group["max_cell_voltage"].rolling(window_size).mean()
    max_voltage_rstd = max_voltage_filtered.rolling(window_size).std()
    max_voltage_rstd_sts = max_voltage_rstd < std_threshold
    max_voltage_rstd_group = (max_voltage_rstd_sts != max_voltage_rstd_sts.shift()).cumsum()  # 连续小于阈值的分为一组
    max_voltage_rstd_group[~max_voltage_rstd_sts] = np.nan

    # 可能存在多个平台，取最后一个
    for _, d_plt in alarm_group.groupby(by=max_voltage_rstd_group):
        plateau_len = len(d_plt)
        if plateau_len < 200:  # 过滤长度200以下，即时长约100分钟的平台
            continue

        max_volt_in_plat_time = d_plt['sample_time'].iloc[0]
        max_volt_in_plat_timestamp = d_plt['sample_timestamp'].iloc[0]

    min_voltage_filtered = alarm_group["min_cell_voltage"].rolling(window_size).mean()
    min_voltage_rstd = min_voltage_filtered.rolling(window_size).std()
    min_voltage_rstd_sts = min_voltage_rstd < std_threshold
    min_voltage_rstd_group = (min_voltage_rstd_sts != min_voltage_rstd_sts.shift()).cumsum()  # 连续小于阈值的分为一组
    min_voltage_rstd_group[~min_voltage_rstd_sts] = np.nan

    # 可能存在多个平台，取最后一个
    for _, d_plt in alarm_group.groupby(by=min_voltage_rstd_group):
        plateau_len = len(d_plt)
        if plateau_len < 200:  # 过滤长度200以下，即时长约100分钟的平台
            continue

        min_volt_in_plat_time = d_plt['sample_time'].iloc[0]
        min_volt_in_plat_timestamp = d_plt['sample_timestamp'].iloc[0]



    alarm_info = defaultdict(list)
    if min_volt_in_plat_timestamp is not None and max_volt_in_plat_timestamp is not None:
        plat_in_time_delta = round(float((min_volt_in_plat_timestamp - max_volt_in_plat_timestamp) / 3600), 3)
        delta_capacity = round(plat_in_time_delta * charge_max_current / capacity_rate * 100 * -1, 2)
        if min_volt_in_plat_timestamp > max_volt_in_plat_timestamp and delta_capacity >= 5:
            if delta_capacity < 10:
                algorithm_id_res = "Algorithm_0fb4b6ba23"
            else:
                algorithm_id_res = algorithm_id

            battery_id = alarm_group.loc[0, "battery_id"]
            device_id = alarm_group.loc[0, "vin"]
            raise_timestamp = int(alarm_group.loc[0, "sample_timestamp"]) * 1000

            device_name = device_id \
                          + '\n里程（km）：' + str(alarm_group.loc[0, "charge_vehicle_mileage"]) \
                          + '\n异常电芯：' + str([alarm_group.loc[0, "min_cell_voltage_sn"]]) \
                          + '\n异常数据：' + str(delta_capacity) + '%'\
                          + '\n最大最小电压进入平台时间差：' + str(plat_in_time_delta) \
                          + '\n最大电压进入平台时间：' + str(max_volt_in_plat_time) \
                          + '\n最小电压进入平台时间：' + str(min_volt_in_plat_time)
            # print(99999999)
            # print(device_name)

            dict_alarm_info = {
                "battery_id": battery_id,  # 电池编号
                "device_id": device_id,  # 设备编号
                "device_name": device_name,  # 设备名称
                "time_stamp": raise_timestamp,  # 采样时间
                "current": alarm_group.loc[0, "current"],  # 总电流
                "voltage": alarm_group.loc[0, "voltage"],  # 总电流
                "soc": alarm_group.loc[0, "user_soc"],  # soc
                "insulation_resistance": alarm_group.loc[0, "vehicle_insulation_resistance"],  # 绝缘阻值
                "max_cell_voltage": alarm_group.loc[0, "max_cell_voltage"],  # 最高单体电压
                "max_cell_voltage_index": alarm_group.loc[0, "max_cell_voltage_sn"],
                # 最高单体电压编号
                "min_cell_voltage": alarm_group.loc[0, "min_cell_voltage"],  # 最低单体电压
                "min_cell_voltage_index": alarm_group.loc[0, "min_cell_voltage_sn"],
                # 最低单体电压编号
                "max_cell_temperature": alarm_group.loc[0, "max_probe_temperature"],  # 最高温度
                "max_cell_temperature_index": alarm_group.loc[0, "max_probe_temperature_sn"],
                # 最高温度编号
                "min_cell_temperature": alarm_group.loc[0, "min_probe_temperature"],  # 最低温度
                "min_cell_temperature_index": alarm_group.loc[0, "min_probe_temperature_sn"],
                # 最低温度编号
            }
            hash_code = gen_hash_code(alarm_id, battery_id, device_id, raise_timestamp)
            alarm_info["algorithm_id"].append(algorithm_id_res)
            alarm_info["algorithm_params_id"].append(algorithm_params_id)
            alarm_info["battery_id"].append(battery_id)
            alarm_info["device_id"].append(device_id)
            alarm_info["process_id"].append('')
            alarm_info["msg_type"].append("periodical_charge_update")
            alarm_info["alarm_data"].append(json.dumps(dict_alarm_info, cls=NpEncoder))
            alarm_info["hash_code"].append(hash_code)
            alarm_info["result_create_time"].append(int(raise_timestamp / 1000))
            etl_time = int(time.time())
            alarm_info["create_time"].append(etl_time)
            alarm_info["update_time"].append(etl_time)
            alarm_info["alarm_id"].append(alarm_id)
            alarm_info["data_source"].append(algorithm.data_type.lower())
            alarm_info["data_type"].append(algorithm.data_type)

    res = res.append(pd.DataFrame(alarm_info), ignore_index=True, sort=False)
    res = res.where(res.notnull(), None)

    if res.shape[0] == 0:
        return [[None] * 14]
    else:
        list_alarms = np.array(res).tolist()
        return list_alarms


def generate_battery_alarm_info():
    """
    按照车辆充高放低算法产生告警数据
    :return: 电池异常预警结果存入Hive表
    """

    # 创建SparkSession, 作为读取数据、处理源数据、配置回话和管理集群资源的入口
    spark = SparkSession.builder \
        .appName("OfflinedCapacitydiffAlarmSvolt") \
        .enableHiveSupport() \
        .getOrCreate()  # prod

    # 算法配置参数
    # 按照企业ID、数据类型、日期读取电池原始数据
    # 对数据进行过滤并转换数据类型
    before_day = (datetime.datetime.strptime(input_date, '%Y%m%d') - datetime.timedelta(days=1)).strftime('%Y%m%d')

    vehicle_model_cover = ["CC7000ZM00GBEV", "CC7000BJ02DBEV", "CC7000CG01ABEV", "CC7000BH02ABEV", "CC6470AH05GPHEV"]
    battery_model_cover = ["09UPB53EQDJ371", "09UPB45MQDYMW3", "09UPB40MQEU823", "09UPB63M343HY2", "0KEPB79P3NJW39"]

    # 按照车型进行过滤
    if vehicle_model_cover == "all":
        vehicle_query_str = ""
    else:
        vehicle_query_list = list()
        for vehicle in vehicle_model_cover:
            vehicle_query_list.append(f"""vehicle_type = '{vehicle}'""")
        vehicle_query_str = "AND (" + " OR ".join(vehicle_query_list) + ")"

    # 按照电池型号体系进行过滤
    if battery_model_cover == "all":
        battery_query_str = ""
    else:
        battery_query_list = list()
        for battery in battery_model_cover:
            battery_query_list.append(f"""battery_model = '{battery}'""")
        battery_query_str = "AND (" + " OR ".join(battery_query_list) + ")"

    sql_read = f"""SELECT
        Distinct CAST(unix_timestamp(sample_time, 'yyyy-MM-dd HH:mm:ss') AS INT) AS sample_timestamp, sample_time,
        vin, battery_id, vehicle_type, battery_model,
        CAST(vehicle_insulation_resistance AS DOUBLE), CAST(voltage AS DOUBLE), CAST(current AS DOUBLE),
        CAST(user_soc AS DOUBLE), CAST(vehicle_mileage AS DOUBLE), vehicle_charge_state,
        max_probe_temperature_sn, CAST(max_probe_temperature AS DOUBLE),
        min_probe_temperature_sn, CAST(min_probe_temperature AS DOUBLE),
        max_cell_voltage_sn, CAST(max_cell_voltage AS DOUBLE),
        min_cell_voltage_sn, CAST(min_cell_voltage AS DOUBLE)
        FROM dw_gb32960_battery.d_i_svolt_battery_detail
        WHERE (date = int({before_day}) or date = int({input_date}))
        {vehicle_query_str}
        {battery_query_str}
        AND (sample_time IS NOT NULL)
        AND (vehicle_charge_state IS NOT NULL)
        AND (current IS NOT NULL)
        AND (user_soc IS NOT NULL)
        AND ((max_cell_voltage > 0) AND (max_cell_voltage < 5000))
        AND ((min_cell_voltage > 0) AND (min_cell_voltage < 5000))
        AND ((max_probe_temperature > -40) AND (max_probe_temperature < 255))
        AND ((min_probe_temperature > -40) AND (min_probe_temperature < 255))"""

    df_detail = spark.sql(sql_read).dropDuplicates(['vin', 'sample_timestamp'])

    # 1 选取隶属于当日的充电数据
    # 1.1 添加上一时刻时间戳
    w1 = Window.partitionBy("vin").orderBy("sample_timestamp")
    df_detail = df_detail.withColumn("vehicle_charge_state_lag", functions.lag(df_detail.vehicle_charge_state).over(w1))
    # 1.2 添加充电起始标志
    df_detail = df_detail \
        .withColumn("charge_start_flag", functions.when(
        (df_detail["vehicle_charge_state"] == 1) &
        (df_detail["vehicle_charge_state"] != df_detail["vehicle_charge_state_lag"]), 1).otherwise(0))

    # 1.3 添加充电次序
    df_detail = df_detail.withColumn("charge_order", functions.sum(df_detail.charge_start_flag).over(w1))

    # 1.4 添加里程信息， 过滤非充电数据
    w2 = Window.partitionBy("vin", "charge_order").orderBy("sample_timestamp")
    w3 = Window.partitionBy("vin", "charge_order").orderBy(functions.desc("sample_timestamp"))

    df_detail = df_detail \
        .withColumn("charge_vehicle_mileage", functions.first(df_detail["vehicle_mileage"], ignorenulls=True).over(w2))

    df_detail = df_detail.filter((df_detail["vehicle_charge_state"] == 1) & (df_detail.current < 0))

    # 1.5 选取慢充数据
    df_detail = df_detail \
        .withColumn("end_timestamp", functions.first(df_detail.sample_timestamp).over(w3)) \
        .withColumn("end_soc", functions.first(df_detail.user_soc).over(w3)) \
        .withColumn("start_soc", functions.first(df_detail.user_soc).over(w2))

    df_detail = df_detail.filter((df_detail["start_soc"] <= 35) & (df_detail["end_soc"] >= 70))

    df_current = df_detail.groupBy("vin", "charge_order").agg(
        functions.mean(df_detail["current"]).alias("charge_mean_current"),
        functions.collect_list(df_detail["current"]).alias("current_list")
    ).withColumnRenamed("vin", "vin_charge").withColumnRenamed("charge_order", "charge_order_charge")

    # 过滤跳变电流的影响
    get_current_lower_boundary = functions.udf(
        lambda x: float(np.quantile(x, 0.25) - 1.5 * (np.quantile(x, 0.75) - np.quantile(x, 0.25))), FloatType())

    get_current_upper_boundary = functions.udf(
        lambda x: float(np.quantile(x, 0.75) + 1.5 * (np.quantile(x, 0.75) - np.quantile(x, 0.25))), FloatType())

    df_current = df_current \
        .withColumn("current_upper_boundary", get_current_upper_boundary(df_current["current_list"])) \
        .withColumn("current_lower_boundary", get_current_lower_boundary(df_current["current_list"]))

    df_current = df_current.select(
            df_current["vin_charge"], df_current["charge_order_charge"],
            df_current["charge_mean_current"],
            df_current["current_upper_boundary"], df_current["current_lower_boundary"]
        )

    cond = [df_detail["vin"] == df_current["vin_charge"],
            df_detail["charge_order"] == df_current["charge_order_charge"]]
    df_detail = df_detail.join(df_current, cond)

    # 过滤异常电流数据和快充数据
    df_detail = df_detail.filter(
        (df_detail["charge_mean_current"] >= -20) & (df_detail["current"] > df_detail["current_lower_boundary"]) &
        (df_detail["current"] < df_detail["current_upper_boundary"])
    ).select(
        df_detail["vin"], df_detail["battery_id"],
        df_detail["vehicle_type"], df_detail["battery_model"], df_detail["charge_order"],
        df_detail["sample_time"], df_detail["sample_timestamp"],
        df_detail["user_soc"], df_detail["voltage"], df_detail["current"], df_detail["vehicle_insulation_resistance"],
        df_detail["max_probe_temperature_sn"], df_detail["max_probe_temperature"],
        df_detail["min_probe_temperature_sn"], df_detail["min_probe_temperature"],
        df_detail["max_cell_voltage_sn"], df_detail["max_cell_voltage"],
        df_detail["min_cell_voltage_sn"], df_detail["min_cell_voltage"],
        df_detail["charge_vehicle_mileage"]
    )
    #
    # print(777777777777)
    # df_detail.show()

    # 进一步分析告警
    def map_alarms(alarms):
        """
        车辆电池单体压差异常告警映射函数
        :param alarms: 计算得到的电池告警列表
        :return: 告警结果
        """
        if isinstance(alarms[1][0], list):
            return alarms[1]
        else:
            list_alarm = [[]]
            for alarm in alarms[1]:
                list_alarm[0].append(alarm)
            return list_alarm

    res = df_detail.rdd \
        .map(lambda x: ((x["vin"], x["charge_order"]), x)) \
        .groupByKey() \
        .mapValues(get_battery_alarm) \
        .flatMap(map_alarms)

    df_alarm = spark.createDataFrame(res, schema=alarmSchema)

    task_time = datetime.datetime.now()
    # 丢弃所有元素均为null的行, 并且将告警结果转化为指定的数据类型
    df_alarm = df_alarm.na.drop(how="all").filter(df_alarm["alarm_id"].isNotNull()) \
        .select(
        df_alarm["alarm_id"].alias("task_id").cast(StringType()),
        functions.lit(task_time).alias("task_time").cast(TimestampType()),
        functions.lit(input_date).alias("data_time").cast(StringType()),
        df_alarm["data_source"].cast(StringType()),
        df_alarm["algorithm_id"].cast(StringType()),
        df_alarm["algorithm_params_id"].cast(StringType()),
        functions.lit(algorithm.enterprise_id).alias("tenant_id").cast(StringType()),
        df_alarm["battery_id"].alias("object_id").cast(StringType()),
        df_alarm["hash_code"].cast(StringType()),
        df_alarm["result_create_time"].alias("result_data_time").cast(TimestampType()),
        functions.struct("device_id", "process_id", "msg_type", "data_type").alias("additional_data"),
        df_alarm["alarm_data"].alias("result_data").cast(StringType()),
        functions.lit(0).alias("notify_status").cast(IntegerType()),
        df_alarm["create_time"].cast(TimestampType()),
        df_alarm["update_time"].cast(TimestampType()),
        functions.lit(functions.current_timestamp()).cast(TimestampType()).alias("dw_etl_time")
    )

    # 将电池告警数据写入Hive数据表
    now_date = datetime.datetime.now().strftime('%Y-%m-%d').replace("-", "")
    df_alarm = df_alarm.repartition(1)
    # print(8888888888)
    # df_alarm.show()
    #
    # 写入指定的HDFS目录
    dm_path = "/data/dw/dm/dm_battery_alarm/d_i_alarm_results"
    table_name = "dm_battery_alarm.d_i_alarm_results"
    df_alarm.write.mode("overwrite").parquet(
        f"{dm_path}/etl_date={now_date}/date={input_date}/algorithm_instance={algorithm_id}",
        mode="overwrite")
    # 关联HDFS目录和HIVE表
    sql_relate = f"""ALTER TABLE {table_name}
           ADD IF NOT EXISTS PARTITION(etl_date='{now_date}',date='{input_date}',algorithm_instance='{algorithm_id}')
           LOCATION '{dm_path}/etl_date={now_date}/date={input_date}/algorithm_instance={algorithm_id}'"""
    spark.sql(sql_relate)
    # 刷新表
    sql_refresh = f"""refresh table {table_name}"""
    spark.sql(sql_refresh)


if __name__ == "__main__":
    """
    入口函数
    :return: 告警数据
    """
    input_date = sys.argv[1]
    input_param = sys.argv[3]
    list_param = input_param.split(",")
    algorithm_id = list_param[0]

    # 获得算法配置参数
    if len(list_param) > 1 and list_param[1] == "test":
        algorithm_env = "test"
    else:
        algorithm_env = "prod"

    # 获取算法输入参数
    algorithm = Algorithm(algorithm_id).init_env(algorithm_env)
    algorithm_params_id = algorithm.algorithm_params_id
    alarm_id = gen_alarm_id(algorithm_id, algorithm_params_id, input_date)

    with proxima(algorithm_id=algorithm_id, env=algorithm_env, date=input_date):
        generate_battery_alarm_info()
