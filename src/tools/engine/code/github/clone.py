#!/usr/bin env python3
#!codeing=utf-8

from src.tools.log4py.log4py import print_log


class CodeClone:
    
    def __init__(self, info: dict=None) -> None:
        
        if info is None:
            return
        self.name = info["name"]
        self.author = info["author"]
        self.version = info["version"]
        self.category = info["category"]
        self.url = info["url"]
        self.branch = info["branch"]
        self.engine = info["engine"]
        self.code_path = info["code_path"]
            
    
    def generate_shell(self) -> str:
        
        shell = f"git clone -b {self.branch} {self.url} {self.code_path}/{self.name}"
        return shell
    
    def abstract_of_description(self) -> str:
        
        info = f"Clone Project {self.name} from {self.url} to {self.code_path}/{self.name}."
        return info
    
    
    def clone(self) -> None:
        
        shell = self.generate_shell()
        print_log(msg=f"{self.abstract_of_description()}", level="DEBUG")
    
    
    def delete(self) -> None:
        
        shell = ""
        if self.code_path != "" or self.code_path is not None:
            shell = f"rm -rf {self.code_path}/{self.name}"
        return shell
    
    
    def update(self) -> None:
        pass
