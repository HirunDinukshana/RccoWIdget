from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QTimer,Qt
import requests
import threading
def random_quotes(fn):
    e= requests.exceptions
    if(not fn):
         print(f"> random quote widget err callback invalid")
         return
    def get():
        try:
            res = requests.get('https://motivational-spark-api.vercel.app/api/quotes/random')
            if res.status_code == 200:
                fn(res.json())
                return
            fn(False)
        except e.ConnectionError or e.ConnectTimeout as err:
            fn({"author":"George Lorimer","quote":"You\u2019ve got to get up every morning with determination if you\u2019re going to go to bed with satisfaction."})
            print(f"> random quote widget err {err}")
    threading.Thread(target=get,daemon=True).start()
            

class RandomQuotesWIdget(QLabel):
    def __init__(self,win,qins):
        self.qins = qins
        super().__init__("Loading Quotes ..",win)
        self.setStyleSheet("""
            border-radius: 6px;
            padding: 6px;
            min-height: 40px;
        """)
        self.setWordWrap(True)
        random_quotes(self.updateText)
        self.updater = QTimer(self)
        self.updater.timeout.connect(lambda : random_quotes(self.updateText))
        self.updater.start((1000 * 60) * 10)
    def updateText(self,text):
        if not text:return
        color = "#888"
        data = f"""
            <div>
                <h2 style="text-align:center;color:{color}">{text['quote']}</h2>
                <p style="text-align:right;color:{color}">{text['author']}</p>
            </div>
        """
        QTimer.singleShot(0,self.qins,lambda : self.setText(data))
    