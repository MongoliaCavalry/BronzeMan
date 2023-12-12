#!/usr/bin/env python3
#!codeing=utf-8

import os
import time

from src.tools.log4py.log4py import print_log
from src.tools.log4py.log4py import LogLevel
from src.model.load_json import load_json_to_dict
from src.tools.engine.code.github.clone import CodeClone
from src.tools.engine.soft.install_soft import SoftTool
from src.tools.engine.env.docker.docker_container_manager import DockerContainerManager
from src.tools.save_monitor_log import save_monitor_log
from src.config.config import configration


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
        
        
    def install_soft(self, file_path: str) -> None:
        
        file_type_code = self.check_file_type(file_path)
        
        if file_type_code == -1:
            # path error
            return
        elif file_type_code == 1:
            # json
            log_info = f"Load soft info from json file: {file_path}."
            print_log(msg=log_info, level=LogLevel.DEBUG)
            json_info = load_json_to_dict(json_file_path=file_path)
            install_soft_tool = SoftTool()
            install_soft_tool.install_soft_by_json(info=json_info)
            return
        elif file_type_code == 2:
            # shell
            install_soft_tool = SoftTool()
            install_soft_tool.install_soft_by_shell(shell_path=file_path)
            pass
        elif file_type_code == 3:
            # python
            pass
        else:
            print_log(msg="ERROR: Unsupported file type.", level=LogLevel.ERROR)
 

    def build_docker_env(self, file_path: str) -> None:
        
        json_info = load_json_to_dict(json_file_path=file_path)
        if json_info.keys() == []:
            print_log(msg="ERROR: Invalid json file.", level=LogLevel.ERROR)
            return
        docker_env = DockerContainerManager(params=json_info)
        docker_env.run()
        
    
    def build_conda_env(self, file_path: str) -> None:
        
        pass
    
    
    def operation(self) -> None:

        monitor_log = []
        file_name = os.path.basename(self.file_path).split(".")[0] + "." + configration.get("monitor_log_file_end")
        time_name = time.strftime("%Y%m%d%H%M%S", time.localtime()) + file_name
        monitor_log.append(f"Time: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        monitor_log.append(f"File path: {self.file_path}")
        
        for item in self.key_words:
            if item == "code":
                info = f"This script need to clone code."
                monitor_log.append(info)
                self.clone_code(file_path=self.file_path)
            if item == "soft":
                info = f"This script need to install soft."
                monitor_log.append(info)
                self.install_soft(file_path=self.file_path)
            if item == "env":
                info = f"This script need to build env."
                monitor_log.append(info)
                if self.key_words[1] == "docker":
                    info = "Build docker env."
                    monitor_log.append(info)
                    print_log(msg=info, level=LogLevel.DEBUG)
                    self.build_docker_env(file_path=self.file_path)
                elif self.key_words[1] == "conda":
                    info = "Build conda env.",
                    monitor_log.append(info)
                    print_log(msg=info, level=LogLevel.DEBUG)
                    self.build_conda_env(file_path=self.file_path)
                elif self.key_words[1] == "java":
                    info = "Build java env."
                    monitor_log.append(info)
                    print_log(msg=info, level=LogLevel.DEBUG)
                else:
                    print_log(msg="ERROR: Unsupported env type.", level=LogLevel.ERROR)
            if item == "action":
                pass
            
        monitor_log.append(f"Finish time: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("--------------")
        for item in monitor_log:
            print(item)
        print("--------------")
        save_monitor_log(monitor_log=monitor_log, log_file_name=time_name)
        
                
    @classmethod
    def check_file_type(cls, file_path) -> int:
        """
        Check the type of the file based on its extension and if it exists.

        Parameters:
        - file_path (str): The path to the file.

        Returns:
        - int: 
            1 if it's a JSON file,
            2 if it's a Shell script file,
            3 if it's a Python file,
            -1 if the file path is invalid or doesn't exist,
            0 for any other file type.
        """

        print_log(msg="Check the type of the file based on its extension and if it exists.", level=LogLevel.DEBUG)
        # Check if the file exists
        if not os.path.exists(file_path):
            log = f"ERROR: The file '{file_path}' does not exist."
            print_log(msg=log, level=LogLevel.ERROR)
            return -1

        # Check the file extension
        _, extension = os.path.splitext(file_path)
        if extension == ".json":
            log = f"INFO: The file '{file_path}' is a JSON file."
            print_log(msg=log, level=LogLevel.DEBUG)
            return 1
        elif extension in [".sh", ".bash"]:
            log = f"INFO: The file '{file_path}' is a Shell file."
            print_log(msg=log, level=LogLevel.DEBUG)
            return 2
        elif extension == ".py":
            log = f"INFO: The file '{file_path}' is a Python file."
            print_log(msg=log, level=LogLevel.DEBUG)
            return 3
        else:
            log = f"WARNING: The file '{file_path}' is of an unknown type."
            print_log(msg=log, level=LogLevel.ERROR)
            return 0
