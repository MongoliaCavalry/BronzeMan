#!/usr/bin env python3
#!codeing=utf-8

from src.tools.log4py.log4py import print_log
from src.tools.os_tools.os_tools import check_os
from src.model.shell_tools import ShellTool
from src.tools.os_tools.generate_log_image_by_chat import generate_char_soft_image


class SoftTool:
    
    def __init__(self) -> None:
        
        pass
    
    @classmethod
    def check_json_keys(cls, json_data: dict) -> bool:
        """
        Check if the provided JSON data has the specified keys.

        Parameters:
        - json_data (dict): The JSON data to be checked.

        Returns:
        - bool: True if all keys exist, False otherwise.
        """
        target_keys = {"name", "version", "liunx_shell_engine", "mac_shell_engine", "engine"}
        return target_keys.issubset(set(list(json_data.keys())))

    
    def generate_install_command_by_json(self, json_data: dict) -> str:
        """
        Generate a shell command to install the target software based on the OS.

        Parameters:
        - json_data (dict): The JSON data containing software details.

        Returns:
        - str: The shell command to install the software.
        """
        os_code = check_os()
        
        shell_str = ""
        
        if not self.check_json_keys(json_data):
            
            log = f"The provided JSON data contains the following keys: {json_data.keys()}"
            print_log(msg=log, level="ERROR")
            return shell_str
        
        engine = json_data.get("engine")
        if engine != "shell":
            log = f"Unsupported engine: {engine}"
            print_log(msg=log, level="ERROR")
            return shell_str
            
        if os_code == 1:
            shell_engine = json_data.get("mac_shell_engine")
        elif os_code == 2:
            shell_engine = json_data.get("liunx_shell_engine")
        elif os_code == 3:
            # Assuming Windows uses a different mechanism or isn't supported based on the provided JSON
            log = "Windows OS detected. Please install manually."
            print_log(msg=log, level="ERROR")
            return shell_str
        else:
            log = "Unsupported OS."
            print_log(msg=log, level="ERROR")
            return shell_str

        if not shell_engine:
            log = "Shell engine not found for the detected OS."
            print_log(msg=log, level="ERROR")
            return shell_str

        shell_str = f"{shell_engine} install {json_data['name']}"
        return shell_str


    def install_soft_by_json(self, info: dict) -> None:
        
        install_command = self.generate_install_command_by_json(json_data=info)
        if install_command != "":
            soft_name = info.get("name")
            log = f"Install command: {install_command}"
            print_log(msg=log, level="DEBUG")
            shell_tools = ShellTool()
            shell_tools.run(cmd=install_command)
            for item in generate_char_soft_image(soft_name, 80, 16):
                print_log(msg=item, level="INFO")
        else:
            log = f"Error json data."
            print_log(msg=log, level="ERROR")
    
    def install_soft_by_shell(self, shell_path: str) -> None:
        
        pass
    
    def uninstall_soft(self) -> None:
        
        pass
    
    def operation(self) -> None:
        
        pass