class  Phone:
    def __init__(self):
        print("I  am  in  Phone Class")

class Samsung(Phone):
    #init
    def __init__(self):
        super().__init__()
        print("I  am  in  Samsung Class")

s= Samsung()