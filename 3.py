class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        Shape.__init__(self)
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

# amina = Rectangle(4, 5)
# amina.area()
# print(amina.area())