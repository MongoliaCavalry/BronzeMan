#!/usr/bin env python3
#!codeing=utf-8

import inspect


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


@inject_file_and_line_number
def print_log(msg: str="", level: str="DEBUG", file_name: str="", line_number: int=-1) -> None:
    
    if level == "DEBUG":
        print(f"[DEBUG][{file_name}:{str(line_number)}] {msg}")
    elif level == "INFO":
        print(msg)
    elif level == "WARNING":
        print(f"[WARNING][{file_name}:{str(line_number)}] {msg}")
    elif level == "ERROR":
        print(msg)
    elif level == "CRITICAL":
        print(msg)
