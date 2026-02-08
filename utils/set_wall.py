import sys
import ctypes
import os
from PySide6.QtCore import QTimer
import random
import threading

current_path = None

def get_path(file):
    global current_path
    if getattr(sys,"frozen",False):
        current_path = sys.executable
    else:
        current_path = file
    current_path = os.path.dirname(current_path)
    return current_path

def get_all_wallpaper(file):
    folder = os.path.join(get_path(file),"wallpapers")
    images = []
    print(current_path)
    for root,dirs,files in os.walk(folder):
        for name in files:
            if name.endswith(".png") or name.endswith(".jpg"):
                images.append(os.path.join(root,name))
    return images

def set_random_wallpaper(file):
    def worker():
        try:
            image_list = get_all_wallpaper(file)
            r = random.randint(0,len(image_list) - 1)
            ctypes.windll.user32.SystemParametersInfoW(20, 0,image_list[r], 0)
        except Exception as e: 
            print(f"> error set wallpaper {e}")
    threading.Thread(target=worker,daemon=True).start()
    