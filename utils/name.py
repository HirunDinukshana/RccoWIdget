from PySide6.QtWidgets import QLabel,QInputDialog
from PySide6.QtCore import QTimer,Qt
from utils.file_handler import file

f = file("user_name.txt")

class NameWidget(QLabel):
    def __init__(self,win,qins):
        self.win = win
        self.qins = qins
        self.name = "RccoLK"
        super().__init__(self.name)
        self.setStyleSheet("""
                        font-size:24pt;
                        color:#ffffff
                        """)
        
        def callback(data):
                self.update_text(data)
        f.read_file(callback)
        
    def update_text(self,data):
        text = f"""RccoLK"""
        if data:
            text = f"""{data}"""
        self.name = text
        QTimer.singleShot(0,self.qins,lambda:self.setText(f"""{text}"""))
        
    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            dialog = QInputDialog(self.win)
            dialog.setWindowTitle("Type the pair")
            dialog.setLabelText("Enter symbol (must end with USDT):")
            dialog.setTextValue(self.name)
            dialog.setStyleSheet("""
                                 
                QLabel{
                    color:#FFFFFF
                }
                QInputDialog {
                    background-color: #1e1e1e;
                    color: #FFFFFF;
                    font-size: 14pt;
                    font-family: Arial;
                }
                QLineEdit {
                    background-color: #2c2c2c;
                    color: #FFFFFF;
                    border: 1px solid #555555;
                    border-radius: 6px;
                    padding: 4px;
                }
                QPushButton {
                    background-color: #444444;
                    color: #FFFFFF;
                    border-radius: 6px;
                    padding: 6px 12px;
                }
                QPushButton:hover {
                    background-color: #666666;
                }
            """)

            if dialog.exec() == QInputDialog.Accepted:
                text = dialog.textValue()
                if len(text) > 0:
                    def updated(data_ok):
                        if data_ok:
                            self.update_text(text)
                    f.write_file(text,updated)
                    

        super().mouseDoubleClickEvent(event)
