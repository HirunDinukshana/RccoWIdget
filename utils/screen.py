class userScreen:
    def __init__(self,screen):
        obj = screen.availableGeometry().getRect()
        self.width = obj[2]
        self.height = obj[3]
    def place_app_on_center(self,app,width,height):
        x = (self.width / 2) - (width / 2)
        y = (self.height / 2) - (height / 2)
        app.setGeometry(x,y,width,height)
    def place_app_on_top_right(self,app,width,height):
        x = (self.width) - (width) - 20
        y = 0
        app.setGeometry(x,y,width,height)
    def place_app_on_bottom_right(self,app,width,height):
        x = (self.width) - (width)
        y = self.height - (height)
        app.setGeometry(x,y,width,height)
    