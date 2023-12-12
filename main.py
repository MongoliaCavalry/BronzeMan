#!/usr/bin/env python3

import multiprocessing
import time
import os

from src.model.load_json import load_json_to_dict
from src.model.load_script import load_script_file
from src.model.shunt import Shunt
from src.tools.engine.code.github.clone import CodeClone
from src.tools.log4py.log4py import print_log
from src.tools.log4py.log4py import LogLevel
from src.tools.engine.soft.install_soft import SoftTool
from src.config.config import configration


def main_process():
    
    print_log(msg=f"Main Process Started: PID {os.getpid()}", level=LogLevel.INFO)
    while True:
        print_log("Main Process is running...")
        folder_path = configration.get("script_path")
        script_type=[".json", ".py", ".shell", "sh"]
        scripts = load_script_file(folder_path=folder_path, script_type=script_type)
        
        print_log(msg="Begin execute scripts.", level=LogLevel.DEBUG)
        for item in scripts:

            print_log(msg=f"Begin run script: {item}.", level=LogLevel.DEBUG)
            
            script_shunt = Shunt(file_path=item, folder_path=folder_path)
            script_shunt.operation()
            print("|")
            print("|")
            print("|")
            
            print_log(msg=f"Run script: {item} over.", level=LogLevel.DEBUG)
            break
        
        time.sleep(configration.get("mian_process_sleep_time", 300))  # 模拟主进程工作
        

def monitor_process():
    while True:
        # 使用进程ID来检查主进程是否存活
        main_process_alive = False
        for process in multiprocessing.active_children():
            if process.name == 'MainProcess':
                main_process_alive = True
                break

        if not main_process_alive:
            print_log(msg="Main Process down! Restarting...", level=LogLevel.ERROR)
            # 重启主进程
            new_main_process = multiprocessing.Process(target=main_process, name='MainProcess')
            new_main_process.start()
        else:
            print_log(mgs=f"Main Process is alive.", level=LogLevel.INFO)

        time.sleep(30)  # 每隔3秒检查一次


if __name__ == "__main__":
    # 创建主进程
    main_proc = multiprocessing.Process(target=main_process, name='MainProcess')
    main_proc.start()

    # 创建监控进程
    monitor_proc = multiprocessing.Process(target=monitor_process)
    monitor_proc.start()

    main_proc.join()
    monitor_proc.join()
        
