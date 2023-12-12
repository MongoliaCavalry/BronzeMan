#!/bin/bash env python3


# Context from Code Snippet src/script/code/github/BronzeMan.json:
# 

import os

from src.tools.log4py.log4py import print_log
from src.tools.log4py.log4py import LogLevel


def load_script_file(folder_path: str, script_type: list=["py", "sh", "shell"]) -> list:
    
    print_log(msg=f"Begin read script file from {folder_path}; and the target file is {script_type}.")
    script_list = []
    try:
        sum = 0
        for filename in os.listdir(folder_path):
            sum = sum + 1
            temp_path = os.path.join(folder_path, filename)
            if os.path.isfile(temp_path):
                if temp_path.endswith(tuple(script_type)):
                    script_list.append(temp_path)
                    print_log(msg=f"find file: {temp_path}", level=LogLevel.DEBUG)
                else:
                    print_log(msg=f"skip file: {temp_path}", level=LogLevel.DEBUG)
            else:
                print_log(msg=f"open fodler: {temp_path}", level=LogLevel.DEBUG)
                temp_files = load_script_file(folder_path=temp_path, script_type=script_type)
                for item in temp_files:
                    script_list.append(os.path.join(folder_path, item))
        if sum == 0:
            print_log(msg="no file found", level=LogLevel.WARNING)
    except Exception:
        print_log("Can't open fodler:" + folder_path)
        return script_list
    return script_list

    
    