class WriteMyStuff():

    def __init__(self) -> None:
        self.text = 'this is a message'
        with open('oop_modules/others/test.txt','a') as f:
            f.write(self.text)

