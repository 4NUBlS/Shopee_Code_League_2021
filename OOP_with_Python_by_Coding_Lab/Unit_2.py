class Rectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def resize(self, factor):
        self.width = self.width * factor
        self.height = self.height * factor

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

smallRect = Rectangle(4, 5)
print(smallRect.height, smallRect.width, smallRect.area())
smallRect.resize(5)
print(smallRect.height, smallRect.width, smallRect.area())