#!/usr/bin env python3
#!codeing=utf-8

import platform


def check_os():
    """
    Check the operating system of the computer.

    Returns:
    - int: 
        1 for Mac OS,
        2 for Linux OS,
        3 for Windows OS,
        0 for any other OS.
    """
    os_mapping = {
        "Darwin": 1,   # Mac OS
        "Linux": 2,    # Linux OS
        "Windows": 3   # Windows OS
    }

    os_name = platform.system()
    return os_mapping.get(os_name, 0)  # Return 0 if OS is not in the mapping
