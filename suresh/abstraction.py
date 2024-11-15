class shape:
    def area(self):
        print("subb class must implemented this method")
    def peri(self):
        print("symbol class must implemented this method")

class rectangle(shape):
    def area(self):
        width=5
        height=10
        return 2*(width*height)
    def peri(self):
        len=5
        bre=10
        return 2*(len+bre)
rect=rectangle()
