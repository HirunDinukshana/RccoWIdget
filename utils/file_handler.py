import os
import threading
appdata = os.getenv("LOCALAPPDATA")
appdata = os.path.join(appdata,"rcco_widget")
class file():
    def __init__(self,file):
        print(appdata)
        self.file = os.path.join(appdata,file)
        
        
    def read_file(self,callback) -> str :
        if(not os.path.exists(self.file)):
            callback(None)
            return
        def read():
            try:
                with open(self.file,"r",encoding="utf-8") as f:
                    read_data = f.read()
                    callback(read_data)
            except Exception as e:
                print(f"> error reading file {self.file}")
                callback(None)
        threading.Thread(target=read,daemon=True).start()
        

    def write_file(self,data,callback):
        if not data:
            callback(False)
            return
        def write():
            try:
                os.makedirs(appdata,exist_ok=True)
                with open(self.file,"w",encoding="utf-8") as f:
                    f.write(data)
                    callback(True)      
            except Exception as e:
                callback(False)
                print(f"> error write to file {self.file}")
        threading.Thread(target=write,daemon=True).start()