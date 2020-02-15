
class Shape:

    def __init__(self):
        IV_type = ""
        IV_colour = ""
        IV_size = {}

    def setColour(self, colour):
        pass

    def getColour(self):
        pass

    def setShapeType(self, shape_type):
        pass
    
    def getShapeType(self):
        pass

    def calculateArea(self):
        pass

class Circle(Shape):

    def setRadius(self, radius):
        pass
    
    def getRadius(self):
        pass

    def calculateArea(self):
        pass

class Square(Shape):
    
    def setLength(self, length):
        pass

    def getLength(self):
        pass

    def calculateArea(self):
        pass

class Rectangle(Shape):

    def setWidth(self, width):
        pass

    def getWidth(self):
        pass

    def setHeight(self, height):
        pass

    def getHeight(self):
        pass

    def calculateArea(self):
        pass

class ShapeManager:

    def getCircleArea(self, radius):
        pass

    def getSquareArea(self, length):
        pass

    def getRectangleArea(self, width, height):
        pass

    def calcuateShapeAreasFromUserInput(self):
        pass