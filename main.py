#!/usr/bin/env python3


from src.model.load_json import load_json_to_dict
from src.model.load_script import load_script_file
from src.model.shunt import Shunt
from src.tools.engine.code.github.clone import CodeClone
from src.tools.log4py.log4py import print_log
from src.tools.engine.soft.install_soft import SoftTool


if __name__ == '__main__':
    
    folder_path = "/Users/pengliu/Code/BronzeMan/src/script"
    script_type=[".json", ".py", ".shell"]
    
    scripts = load_script_file(folder_path=folder_path, script_type=script_type)
    
    print_log(msg="Begin execute scripts.", level="DEBUG")
    for item in scripts:
        print_log(msg=f"Begin run script: {item}.", level="DEBUG")
        
        script_shunt = Shunt(file_path=item, folder_path=folder_path)
        script_shunt.operation()
        
        
        print_log(msg=f"Run script: {item} over.", level="DEBUG")
        
        
