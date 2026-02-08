import os
import sys
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtCore import QTimer
from datetime import datetime

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class ClockWidget(QLabel):
    def __init__(self, win):
        super().__init__("", win)
        self.win = win
        
        font_path = resource_path("utils/fonts/Branda-yolq.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)
        
        if font_id == -1:
            raise Exception(f"> font loading error at: {font_path}")
            
        self.font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        self.setStyleSheet("""
            color: #FFFFFFCC;
            border-radius: 15px;
            padding: 15px;
        """)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.update_time()

    def start(self):
        self.timer.start(5000)

    def stop(self):
        self.timer.stop()

    def update_time(self):
        now = datetime.now()
        time_str = now.strftime("%H:%M")
        seconds_str = now.strftime("%S")
        weekday_str = now.strftime("%A")
        date_str = now.strftime("%d %b %Y")
        
        self.setText(f"""
        <div align="center" style="">
            <div style="font-family:'{self.font_family}'; font-size:16pt;">
            <center>{date_str}</center>
            </div>
            <center>
                <div style="font-family:'Arial'; font-size:64pt; font-weight:bold;">
                    <p>{time_str}</p>
                </div>
            </center>
            <div style="font-family:'{self.font_family}'; font-size:18pt; font-weight:bold;">{weekday_str}</div>
        </div>
        """)

    def place_on_the_center(self, width, height):
        x = (width - self.width()) / 2
        y = (height - self.height()) / 2
        self.move(x, y)