#!/usr/bin/env python3
#!codeing=utf-8

import os

from src.tools.log4py.log4py import print_log
from src.model.load_json import load_json_to_dict
from src.tools.engine.code.github.clone import CodeClone
from src.tools.engine.soft.install_soft import SoftTool
from src.tools.engine.env.docker.docker_container_manager import DockerContainerManager

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
            print_log(msg=log_info, level="DEBUG")
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
            print_log(msg="ERROR: Unsupported file type.", level="ERROR")
 

    def build_docker_env(self, file_path: str) -> None:
        
        json_info = load_json_to_dict(json_file_path=file_path)
        if json_info.keys() == []:
            print_log(msg="ERROR: Invalid json file.", level="ERROR")
            return
        docker_env = DockerContainerManager(params=json_info)
        docker_env.run()
        
    
    def build_conda_env(self, file_path: str) -> None:
        
        pass
    
    
    def operation(self) -> None:

        for item in self.key_words:
            if item == "code":
                self.clone_code(file_path=self.file_path)
            if item == "soft":
                self.install_soft(file_path=self.file_path)
            if item == "env":
                if self.key_words[1] == "docker":
                    print_log(msg="Build docker env.", level="DEBUG")
                    self.build_docker_env(file_path=self.file_path)
                elif self.key_words[1] == "conda":
                    print_log(msg="Build conda env.", level="DEBUG")
                    self.build_conda_env(file_path=self.file_path)
                elif self.key_words[1] == "java":
                    print_log(msg="Build java env.", level="DEBUG")
                else:
                    print_log(msg="ERROR: Unsupported env type.", level="ERROR")
            if item == "action":
                pass
        
                
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

        print_log(msg="Check the type of the file based on its extension and if it exists.", level="DEBUG")
        # Check if the file exists
        if not os.path.exists(file_path):
            log = f"ERROR: The file '{file_path}' does not exist."
            print_log(msg=log, level="ERROR")
            return -1

        # Check the file extension
        _, extension = os.path.splitext(file_path)
        if extension == ".json":
            log = f"INFO: The file '{file_path}' is a JSON file."
            print_log(msg=log, level="DEBUG")
            return 1
        elif extension in [".sh", ".bash"]:
            log = f"INFO: The file '{file_path}' is a Shell file."
            print_log(msg=log, level="DEBUG")
            return 2
        elif extension == ".py":
            log = f"INFO: The file '{file_path}' is a Python file."
            print_log(msg=log, level="DEBUG")
            return 3
        else:
            log = f"WARNING: The file '{file_path}' is of an unknown type."
            print_log(msg=log, level="ERROR")
            return 0
