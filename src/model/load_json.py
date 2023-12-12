#!/usr/bin/env python3
#!codeing=utf-8

import json

from src.tools.log4py.log4py import print_log
from src.tools.log4py.log4py import LogLevel



def load_json_to_dict(json_file_path: str) -> dict:
    
    print_log(msg=f"load json file: {json_file_path}", level=LogLevel.DEBUG)
    data = {}
    with open(json_file_path, 'r') as file:
        try:
            data = json.load(file)
        except Exception as e:
            print_log(msg=f"load json file error: {e}", level=LogLevel.ERROR)
    return data

