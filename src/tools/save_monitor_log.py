#!/usr/bin env python3
#!codeing=utf-8

import os

from src.config.config import configration


def save_monitor_log(monitor_log: list = None, log_file_name: str = "monitor.log") -> None:
    # 获取日志文件夹路径
    folder = configration.get("monitor_log_folder_path", ".")

    # 确保logs是一个列表
    if monitor_log is None:
        monitor_log = []

    # 确保文件夹路径存在
    os.makedirs(folder, exist_ok=True)

    # 完整的日志文件路径
    log_file_path = os.path.join(folder, log_file_name)

    # 将日志写入文件
    with open(log_file_path, 'a') as file:  # 使用'a'模式以追加内容
        for log in monitor_log:
            file.write(log + '\n')
