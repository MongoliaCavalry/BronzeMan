#!/usr/bin/env python3


from src.model.load_json import load_json_to_dict
from src.model.load_script import load_script_file
from src.tools.engine.code.github.clone import CodeClone
from src.tools.log4py.log4py import print_log


if __name__ == '__main__':
    
    folder_path = "/Users/pengliu/Code/BronzeMan/src/script"
    script_type=["json", "py", "shell"]
    
    scripts = load_script_file(folder_path=folder_path, script_type=script_type)
    
    print_log(msg="Begin execute scripts.", level="DEBUG")
    for item in scripts:
        print_log(msg=f"Begin run script: {item}.", level="DEBUG")
        
        
        json_info = load_json_to_dict(json_file_path=item)
        code_clone = CodeClone(info=json_info)
        code_clone.clone()
        
        print_log(msg=f"Run script: {item} over.", level="DEBUG")
        
        