#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import subprocess

from src.tools.log4py.log4py import print_log
from src.tools.log4py.log4py import LogLevel
from src.config.config import key_of_run_shell


class ShellTool:
    
    def __init__(self) -> None:
        
        pass


    def run(self, cmd: str=None, stderr: bool=True, not_print: bool=False) -> str:
        
        if not_print:
            cmd = self.no_print(cmd=cmd)
        print_log(msg="执行<" + cmd + ">...", level=LogLevel.DEBUG)
        if (key_of_run_shell):
            print_log(msg=f"", level=LogLevel.DEBUG)
            result = subprocess.run(args=cmd, timeout=300, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if stderr:  
                return str(result.stdout.decode('utf-8'))
            return str(result.stderr.decode('utf-8'))
        else:
            return ""

    
    def no_print(cls, cmd: str) -> str:
        
        return f"{cmd} 1>/dev/null"
        