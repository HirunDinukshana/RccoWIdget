from PySide6.QtWidgets import QSystemTrayIcon,QMenu 
from PySide6.QtGui import QIcon
import os,sys

def get_path(file):
    global current_path
    if getattr(sys,"frozen",False):
        current_path = sys.executable
    else:
        current_path = file
    current_path = os.path.dirname(current_path)
    return current_path

class appTray(QSystemTrayIcon):
    def __init__(self,file):
        super().__init__()
        self.setIcon(QIcon(os.path.join(get_path(file),"app_icon.png")))
    def set_tray_menu(self):
        menu = QMenu()
        quite = menu.addAction("Quit")
        self.setContextMenu(menu)
        quite.triggered.connect(self.quite_fn)
    def set_menu_item_func(self,quite_fn):
        self.quite_fn = quite_fn