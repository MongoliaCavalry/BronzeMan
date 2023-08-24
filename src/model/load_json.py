#!/usr/bin/env python3
#!codeing=utf-8

import json

from src.tools.log4py.log4py import print_log


def load_json_to_dict(json_file_path: str) -> dict:
    
    print_log(msg=f"load json file: {json_file_path}", level="DEBUG")
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    return data

