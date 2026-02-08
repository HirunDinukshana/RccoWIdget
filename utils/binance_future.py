import requests
import threading
from utils.Exceptions import CoinNotFound,HttpError
import json
from PySide6.QtWidgets import QLabel,QInputDialog
from PySide6.QtCore import Qt,QTimer
import os

appdata = os.getenv("LOCALAPPDATA")

def FutureGet(coin,function,qins,timeout=5):
    def get():
        try:
            response = requests.get("https://fapi.binance.com/fapi/v1/ticker/24hr",timeout=timeout)
            if(response.status_code == 200):
                j = response.json()
                save_btc = None
                for i in range(len(j)):
                    if(j[i]["symbol"]) == "BTCUSDT":
                        save_btc = j[i]
                    if (j[i]["symbol"]) == coin:
                        QTimer.singleShot(0,qins,lambda:function(j[i]))
                        return
                QTimer.singleShot(0,qins,lambda:function(save_btc))
            else:
                print("> error futureRequest")
                raise HttpError("error futureRequest")
        except requests.exceptions.ConnectionError as e:
            trash_data ={
                    "symbol":"NetWorkErr",
                    "lastPrice":0,
                    "priceChange":0,
                    "priceChangePercent":"0%",
                    "highPrice":100,
                    "lowPrice":100,
                    "volume":0,
                    "quoteVolume":0
                    }
            QTimer.singleShot(0,qins,lambda:function(trash_data))
            return
    threading.Thread(target=get,daemon=True).start()
  
    
class FutureWidget(QLabel):
    def __init__(self, win, qins):
        super().__init__("", win)
        self.win = win
        self.pair = self.load_data()
        self.qins = qins
        try:
            FutureGet(self.pair, self.setCoin, qins)
        except CoinNotFound:
            self.pair = "BTCUSDT"

        self.updater = QTimer(self)
        self.updater.timeout.connect(lambda: FutureGet(self.pair, self.setCoin, qins))
        self.updater.start(1000 * 60)

    def load_data(self):
        path = os.path.join(appdata,"rcco_widget")
        try:
            if(os.path.exists(os.path.join(path,"future_widget.txt"))):    
                with open(os.path.join(path,"future_widget.txt"),"r",encoding="utf-8") as f:
                    return f.read()
            return "BTCUSDT"
        except Exception as e:
            print("> load_data fail at futureWidget")

    def setCoin(self, data):
        price_change = float(data["priceChange"])
        change_color = "#FF3B3B" if price_change < 0 else "#00FF99"

        self.setText(f"""
                     <br>
        <div  align="center" style="width:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; padding:12pt">
            <h1 style="margin:0; color:#FFFFFFCC; font-size:28px;">{data["symbol"]}</h1>
            <p style="margin:2px 0; color:#FFFFFFCC; font-size:24px;">{data["lastPrice"]}</p>
            <p style="margin:2px 0; color:{change_color}; font-size:18px;">
                {data['priceChange']} ({data['priceChangePercent']}%)
            </p>
            <p style="margin:2px 0; color:#CCCCFF; font-size:14px;">
                High: {data['highPrice']}  Low: {data['lowPrice']}
            </p>
            <p style="margin:2px 0; color:#CCCCCC; font-size:10px;">
                Vol: {float(data['volume']):,.2f}  Quote: {float(data['quoteVolume']):,.2f}
            </p>
        </div>
        """)

    def place_below_clock(self, clock_widget, y_offset=10):
        """Place FutureWidget below clock_widget, horizontally aligned"""
        x = clock_widget.x() + (clock_widget.width() - self.width()) / 2
        y = clock_widget.y() + clock_widget.height() + y_offset
        self.move(x, y)

    def write_to_file(self,data):
        if not data:
            return
        path = os.path.join(appdata,"rcco_widget")
        print(path)
        os.makedirs(path,exist_ok=True)
        def write():
            try:
                with open(os.path.join(path,"future_widget.txt"),"w",encoding="utf-8") as f:
                    f.write(data)
            except Exception as e:
                print(f"> error write_to_file at FutureWidget {e}")
        threading.Thread(target=write,daemon=True).start()
            

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            dialog = QInputDialog(self.win)
            dialog.setWindowTitle("Type the pair")
            dialog.setLabelText("Enter symbol (must end with USDT):")
            dialog.setTextValue(self.pair)
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
                    self.pair = text
                    self.write_to_file(self.pair)
                    FutureGet(self.pair, self.setCoin, self.qins)
                    

        super().mouseDoubleClickEvent(event)
