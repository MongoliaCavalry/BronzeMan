#!/usr/bin/env python3
#!codeing=utf-8

from src.tools.log4py.log4py import print_log
from src.model.load_json import load_json_to_dict
from src.tools.engine.code.github.clone import CodeClone


class Shunt:
    
    
    def __init__(self, file_path: str, folder_path: str) -> None:
        
        sub_str = file_path.replace(folder_path, "")
        self.file_path = file_path
        self.key_words = list(filter(lambda x: x != "", sub_str.split("/")))
        print_log(msg=str(self.key_words))
        
    
    def clone_code(self, file_path: str) -> None:
        
        json_info = load_json_to_dict(json_file_path=file_path)
        code_clone = CodeClone(info=json_info)
        code_clone.clone()
        
    def install_soft(self) -> None:
        
        pass
    
    
    def build_env(self) -> None:
        
        pass
    
    
    def operation(self) -> None:
        
        for item in self.key_words:
            if item == "code":
                self.clone_code(file_path=self.file_path)
            if item == "soft":
                pass
            if item == "env":
                pass
            if item == "action":
                pass
        