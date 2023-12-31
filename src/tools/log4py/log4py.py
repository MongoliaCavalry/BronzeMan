#!/usr/bin env python3
#!codeing=utf-8

import inspect
from datetime import datetime
from termcolor import colored
from enum import Enum
from src.config.config import configration
from src.config.config import key_of_log_add_file_line_info


class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5
    
    
def get_now_date_time() -> str:
    """get_now_date_time

    Returns:
        str: date time
    """
    
    # Get current date and time
    now = datetime.now()
    formatted_date_time = now.strftime('%Y-%m-%d %H:%M:%S')
    date_time = str(formatted_date_time)
    return date_time


def inject_file_and_line_number(func):
    
    def wrapper(*args, **kwargs):
        
        frame = inspect.currentframe()
        # 获取调用装饰器的代码的上一帧（调用代码）的信息
        calling_frame_info = inspect.getouterframes(frame)[1]
        file_name = calling_frame_info.filename
        line_number = calling_frame_info.lineno

        
        kwargs["file_name"] = file_name
        kwargs["line_number"] = line_number
        
        # print(f"args type: {str(type(args))}")
        # print(args)
        # print(f"kwargs type: {str(type(kwargs))}")
        # print(kwargs)

        func(*args, **kwargs)
        
    return wrapper


def save_log(log_message: str, log_file_path: str):
    """
    Save a log message to the specified log file.

    Parameters:
    - log_message (str): The message to be logged.
    - log_file_path (str): The path to the log file.

    Returns:
    - None
    """
    with open(log_file_path, 'a') as log_file:
        log_file.write(log_message + '\n')



@inject_file_and_line_number
def print_log(msg: str="", level: LogLevel=LogLevel.DEBUG, file_name: str="", line_number: int=-1) -> None:
    
    date_time = get_now_date_time()
    info = msg
    file_info = "At:" + file_name + ":" + str(line_number)
    if not key_of_log_add_file_line_info:
        file_info = ""
    if level == LogLevel.DEBUG:
        info = f"{date_time} DEBUG {msg} {file_info}."
        info = colored(info, 'green')
    elif level == LogLevel.INFO:
        info = f"{date_time} INFO {msg} {file_info}."
        info = colored(info, 'blue')
    elif level == LogLevel.WARNING:
        info = f"{date_time} WARNING {msg} {file_info}."
        info = colored(info, 'y')
    elif level == LogLevel.ERROR:
        info = f"{date_time} ERROR {msg} {file_info}."
        info = colored(info, 'red')
    elif level == LogLevel.CRITICAL:
        pass
    print(info)
    log_path = configration.get("log_path")
    save_log(log_message=info, log_file_path=log_path)
