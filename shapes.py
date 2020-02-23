
import math

class RDK:
    success = "success"
    return_msg = "return_msg"
    debug_data = "debug_data"
 
class RC:
    failed = False
    success = True
    input_validation = 1001
    non_overwritten_virtual = 2002


def log_exception(function_name=None, action_description=None, exception_object=None):
    if type(function_name) != str:
        function_name = "Not Specified"
    if type(action_description) != str:
        action_description = "Not Specified"

    try:
        e_str = str(exception_object)
    except:
        e_str = "could not convert exception to string"

    output_string = 'expection occured in function: ' + function_name + '. while trying to: ' + action_description + ' .exception:' + e_str
    return output_string

class Shape:

    def __init__(self):
        self.IV_type = ""
        self.IV_colour = ""
        self.IV_size = {}

    def setColour(self, colour):
        return_msg = "Shape:setColour: "
        debug_data = []

        ## input validation
        
        if type(colour) is not str:
            return_msg += "input colour is not of type `str` its {}".format(type(colour))
            return {RDK.success: RC.input_validation, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

        if colour not in ("red", "green", "blue"):
            return_msg += "input colour \"{}\"is not valid colour".format(colour)
            return {RDK.success: RC.input_validation, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

        ##</end> input validation

        self.IV_colour = colour

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def getColour(self):
        return_msg = "Shape:getColour: "
        debug_data = []

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "colour": self.IV_colour}

    def setShapeType(self, shape_type):
        return_msg = "Shape:setShapeType: "
        debug_data = []

        ## input validation

        if type(shape_type) is not str:
            return_msg += "input colour is not of type `str`; is type {}".format(type(shape_type))
            return {RDK.success: RC.input_validation, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

        if shape_type not in ("circle", "square", "rectangle"):
            return_msg += "input shape \"{}\"is not valid shape".format(shape_type)
            return {RDK.success: RC.input_validation, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

        ##</end> input validation

        self.IV_type = shape_type

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}
    
    def getShapeType(self):
        return_msg = "Shape:getShapeType: "
        debug_data = []

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "type": self.IV_type}

    def calculateArea(self):
        return_msg = "Shape:calculateArea: "
        debug_data = []
        area = 0

        return_msg += "function not overwritten by leaf class"

        return {RDK.success: RC.non_overwritten_virtual, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

class Circle(Shape):

    def __init__(self):
        super().__init__()
        self.IV_type = "circle"
        self.IV_size["radius"] = 1

    def setRadius(self, radius):
        return_msg = "Circle:setRadius: "
        debug_data = []

        ## input validation

        if type(radius) is not float:
            return_msg += "input radius is not of type `float`; is type {}".format(type(radius))
            return {RDK.success: RC.input_validation, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

        ##</end> input validation
        
        self.IV_size["radius"] = radius

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}
    
    def getRadius(self):
        return_msg = "Circle:getRadius: "
        debug_data = []

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "radius": self.IV_size["radius"]}

    def calculateArea(self):
        return_msg = "Circle:calculateArea: "
        debug_data = []
        area = 0

        area = math.pi * self.IV_size["radius"] ** 2

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

class Square(Shape):

    def __init__(self):
        super().__init__()
        self.IV_type = "square"
        self.IV_size["length"] = 1
    
    def setLength(self, length):
        return_msg = "Square:setLength: "
        debug_data = []

        ## input validation

        if type(length) is not float:
            return_msg += "input length is not of type `float`; is type {}".format(type(length))
            return {RDK.success: RC.input_validation, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

        ##</end> input validation

        self.IV_size["length"] = length

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def getLength(self):
        return_msg = "Square:getLength: "
        debug_data = []

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "length": self.IV_size["length"]}

    def calculateArea(self):
        return_msg = "Square:calculateArea: "
        debug_data = []
        area = 0

        area = self.IV_size["length"] ** 2

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

class Rectangle(Shape):

    def __init__(self):
        super().__init__()
        self.IV_type = "rectangle"
        self.IV_size["width"] = 1
        self.IV_size["height"] = 1

    def setWidth(self, width):
        return_msg = "Rectangle:calculateArea: "
        debug_data = []

        ## input validation

        if type(width) is not float:
            return_msg += "input width is not of type `float`; is type {}".format(type(width))
            return {RDK.success: RC.input_validation, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

        ##</end> input validation

        self.IV_size["width"] = width

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def getWidth(self):
        return_msg = "Rectangle:getWidth: "
        debug_data = []

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "width": self.IV_size["width"]}

    def setHeight(self, height):
        return_msg = "Rectangle:setHeight: "
        debug_data = []

        ## input validation

        if type(height) is not float:
            return_msg += "input height is not of type `float`; is type {}".format(type(height))
            return {RDK.success: RC.input_validation, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

        ##</end> input validation

        self.IV_size["height"] = height

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def getHeight(self):
        return_msg = "Rectangle:getHeight: "
        debug_data = []

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "height": self.IV_size["height"]}

    def calculateArea(self):
        return_msg = "Rectangle:calculateArea: "
        debug_data = []
        area = 0

        area = self.IV_size["width"] * self.IV_size["height"]

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

class ShapeManager:

    def getCircleArea(self, radius):
        return_msg = "ShapeManager:getCircleArea: "
        debug_data = []
        call_result = {}
        area = 0

        ## input validation

        if type(radius) is not float:
            return_msg += "input radius is not of type `float`; is type {}".format(type(radius))
            return {RDK.success: RC.input_validation, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

        ##</end> input validation

        ## circle creation

        circle = Circle()
        call_result = circle.setRadius(radius)
        debug_data.append(call_result)

        call_result = circle.calculateArea()
        debug_data.append(call_result)

        for entry in debug_data:
            if entry[RDK.success] is not RC.success:
                return {RDK.success: entry[RDK.success], RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

        ##</end> circle creation

        area = call_result["area"]

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

    def getSquareArea(self, length):
        return_msg = "ShapeManager:getSquareArea: "
        debug_data = []
        call_result = {}
        area = 0

        ## input validation

        if type(length) is not float:
            return_msg += "input length is not of type `float`; is type {}".format(type(length))
            return {RDK.success: RC.input_validation, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

        ##</end> input validation

        ## square creation

        square = Square()
        call_result = square.setLength(length)
        debug_data.append(call_result)

        call_result = square.calculateArea()
        debug_data.append(call_result)

        for entry in debug_data:
            if entry[RDK.success] is not RC.success:
                return {RDK.success: entry[RDK.success], RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

        ##</end> square creation

        area = call_result["area"]

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

    def getRectangleArea(self, width, height):
        return_msg = "ShapeManager:getRectangleArea: "
        debug_data = []
        call_result = {}
        area = 0

        ## input validation

        if type(width) is not float:
            return_msg += "input width is not of type `float`; is type {}".format(type(width))
            return {RDK.success: RC.input_validation, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

        ##</end> input validation

        ## rectangle creation

        rectangle = Rectangle()
        call_result = rectangle.setWidth(width)
        debug_data.append(call_result)
        
        call_result = rectangle.setHeight(height)
        debug_data.append(call_result)

        call_result = rectangle.calculateArea()
        debug_data.append(call_result)

        for entry in debug_data:
            if entry[RDK.success] is not RC.success:
                return {RDK.success: entry[RDK.success], RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

        ##</end> rectangle creation

        area = call_result["area"]

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

    def calcuateShapeAreasFromUserInput(self):
        return_msg = "ShapeManager:calcuateShapeAreasFromUserInput: "
        debug_data = []
        call_result = {}
        radius = 0
        length = 0
        width = 0
        height = 0
        area = 0

        shape = None

        ## input gathering and validation

        shape_type = input("Enter the type of shape or \"exit\" to exit: ")
        if shape_type == "circle":
            shape = Circle()

            radius = float(input("Enter radius of circle: "))

            call_result = shape.setRadius(radius)
            debug_data.append(call_result)

            if call_result[RDK.success] is not RC.success:
                return {RDK.success: call_result[RDK.success], RDK.return_msg: return_msg, RDK.debug_data: debug_data}

        elif shape_type == "square":
            shape = Square()

            length = float(input("Enter length of square: "))

            call_result = shape.setLength(length)
            debug_data.append(call_result)

            if call_result[RDK.success] is not RC.success:
                return {RDK.success: call_result[RDK.success], RDK.return_msg: return_msg, RDK.debug_data: debug_data}


        elif shape_type == "rectangle":
            shape = Rectangle()
            return_msg += "shape type rectangle"

            width = float(input("Enter width of rectangle: "))
            height = float(input("Enter height of rectangle: "))

            call_result = shape.setWidth(width)
            debug_data.append(call_result)

            call_result = shape.setHeight(height)
            debug_data.append(call_result)

            for entry in debug_data:
                if entry[RDK.success] is not RC.success:
                    return {RDK.success: entry[RDK.success], RDK.return_msg: return_msg, RDK.debug_data: debug_data}

        elif shape_type in ("quit", "exit"):
            return_msg += "user exited function"
            return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

        else:
            return_msg += "invalid shape type \"{}\"".format(shape_type)
            print("\"{}\" is not a valid shape".format(shape_type))

            return {RDK.success: RC.input_validation, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

        ##</end> input gathering

        ## area calculation

        call_result = shape.calculateArea()
        debug_data.append(call_result)

        for entry in debug_data:
                if entry[RDK.success] is not RC.success:
                    return {RDK.success: entry[RDK.success], RDK.return_msg: return_msg, RDK.debug_data: debug_data}

        area = call_result["area"]

        print("Area of %s is %g" % (str(shape.getShapeType()["type"]), area))

        ##</end> area calculation

        return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

## tests

def test_circle():
    circle = Circle()

    assert circle.setRadius(1.0)[RDK.success]
    area = circle.calculateArea()["area"]
    assert math.isclose(area, math.pi)

    assert circle.setRadius(4.0)[RDK.success]
    area = circle.calculateArea()["area"]
    assert math.isclose(area, 50.26548245743668985596741549670696258544921875)

    assert circle.setRadius(14.0)[RDK.success]
    area = circle.calculateArea()["area"]
    assert math.isclose(area, 615.752160103599408103036694228649139404296875)

    assert circle.setRadius(48.0)[RDK.success]
    area = circle.calculateArea()["area"]
    assert math.isclose(area, 7238.2294738708833392593078315258026123046875)

def test_square():
    square = Square()

    assert square.setLength(1.0)[RDK.success]
    area = square.calculateArea()["area"]
    assert math.isclose(area, 1.0)

    assert square.setLength(4.0)[RDK.success]
    area = square.calculateArea()["area"]
    assert math.isclose(area, 16.0)

    assert square.setLength(14.0)[RDK.success]
    area = square.calculateArea()["area"]
    assert math.isclose(area, 196.0)

    assert square.setLength(48.0)[RDK.success]
    area = square.calculateArea()["area"]
    assert math.isclose(area, 2304.0)

def test_rectangle():
    rectangle = Rectangle()

    assert rectangle.setWidth(1.0)[RDK.success]
    assert rectangle.setHeight(1.0)[RDK.success]
    area = rectangle.calculateArea()["area"]
    assert math.isclose(area, 1.0)

    assert rectangle.setWidth(4.0)[RDK.success]
    assert rectangle.setHeight(14.0)[RDK.success]
    area = rectangle.calculateArea()["area"]
    assert math.isclose(area, 56.0)

    assert rectangle.setWidth(14.0)[RDK.success]
    assert rectangle.setHeight(4.0)[RDK.success]
    area = rectangle.calculateArea()["area"]
    assert math.isclose(area, 56.0)

    assert rectangle.setWidth(48.0)[RDK.success]
    assert rectangle.setHeight(14.0)[RDK.success]
    area = rectangle.calculateArea()["area"]
    assert math.isclose(area, 672.0)

    assert rectangle.setWidth(14.0)[RDK.success]
    assert rectangle.setHeight(48.0)[RDK.success]
    area = rectangle.calculateArea()["area"]
    assert math.isclose(area, 672.0)

def test():
    test_circle()
    test_square()
    test_rectangle()

##</end> tests

## main program
if __name__ == "__main__":
    test()
    manager = ShapeManager()
    loop = True
    while loop:
        user_result = manager.calcuateShapeAreasFromUserInput()
        if "exited" in user_result[RDK.return_msg]:
            print("Exiting...")
            loop = False

##</end> main program