class String():
    def _init_(self):
        self.chars = ""

    def getString(self):
        self.chars = input()

    def printString(self):
        print(self.chars.upper())
        
s = String()
s.getString()
s.printString()
