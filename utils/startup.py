import os
import sys
import winreg

def add_to_startup_once(app_name="MyPythonApp"):
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run"
        )
        winreg.QueryValueEx(key, app_name)
        winreg.CloseKey(key)
        return  # already registered
    except FileNotFoundError:
        pass

    if getattr(sys, "frozen", False):
        app_path = sys.executable
    else:
        app_path = os.path.abspath(__file__)

    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0,
        winreg.KEY_SET_VALUE
    )
    winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, app_path)
    winreg.CloseKey(key)

