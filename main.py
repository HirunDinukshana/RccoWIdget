from utils.screen import userScreen
from utils.tray import appTray as appTray_util
from utils.clock import ClockWidget
from utils.binance_future import FutureGet,FutureWidget
from utils.name import NameWidget
from utils.random_quotes import RandomQuotesWIdget
from utils.startup import add_to_startup_once
from utils.set_wall import set_random_wallpaper

import sys
from PySide6.QtWidgets import QApplication,QWidget,QGridLayout
from PySide6.QtCore import Qt


add_to_startup_once()
set_random_wallpaper(__file__)

APP_WIDTH = 500
APP_HEIGHT = 500

#grid
grid = QGridLayout()

#init qApplication
app = QApplication(sys.argv)

#init userScreenObj
screen_util = userScreen(app.primaryScreen())


#create q windows
win = QWidget()
#Qt.FramelessWindowHint Qt.WindowStaysOnTopHint
win.setWindowFlag( Qt.Tool | Qt.FramelessWindowHint )
win.setAttribute(Qt.WA_TranslucentBackground)
win.setLayout(grid)

screen_util.place_app_on_top_right(win,APP_WIDTH,APP_HEIGHT)

#clock Widget
clockWidget = ClockWidget(win)
clockWidget.start()
grid.addWidget(clockWidget,0,0,alignment=Qt.AlignTop | Qt.AlignLeft)

futureWidget = FutureWidget(win,app.instance())
grid.addWidget(futureWidget,0,1,alignment=Qt.AlignTop | Qt.AlignLeft)

nameWidget = NameWidget(win,app.instance())
grid.addWidget(nameWidget,1,0,1,2)

randomQuotesWidget = RandomQuotesWIdget(win,QApplication.instance())
grid.addWidget(randomQuotesWidget,2,0,1,2)

def app_close():
    clockWidget.stop()
    app.quit()

#add system tray 
system_tray = appTray_util(__file__)
system_tray.set_menu_item_func(app_close)
system_tray.set_tray_menu()
system_tray.show()


win.show()
sys.exit(app.exec())