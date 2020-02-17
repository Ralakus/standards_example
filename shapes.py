
import math

class RDK:
    success = "success"
    return_msg = "return_msg"
    debug_data = "debug_data"
 
class RC:
    failed = False
    success = True
    input_validation = 1001


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
        success = RC.failed

        ## input validation

        if type(colour) is not str:
            return_msg += "input colour is not of type `str`"
        elif colour not in ("red", "green", "blue"):
            return_msg += "input colour \"%s\"is not valid colour" % colour
        else:
            self.IV_colour = colour
            return_msg += "colour successfully set to %s" % colour
            success = RC.success

        ##</end> input validation

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def getColour(self):
        return_msg = "Shape:getColour: "
        debug_data = []
        success = RC.success

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "colour": self.IV_colour}

    def setShapeType(self, shape_type):
        return_msg = "Shape:setShapeType: "
        debug_data = []
        success = RC.failed

        ## input validation

        if type(shape_type) is not str:
            return_msg += "input colour is not of type `str`"
        elif shape_type not in ("circle", "square", "rectangle"):
            return_msg += "input shape \"%s\"is not valid shape" % shape_type
        else:
            self.IV_type = shape_type
            success = RC.success
            return_msg += "shape successfully set to %s" % shape_type

        ##</end> input validation

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}
    
    def getShapeType(self):
        return_msg = "Shape:getShapeType: "
        debug_data = []
        success = RC.success

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "type": self.IV_type}

    def calculateArea(self):
        return_msg = "Shape:calculateArea: "
        debug_data = []
        success = RC.failed

        return_msg += "function not overwritten by leaf class"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

class Circle(Shape):

    def __init__(self):
        super().__init__()
        self.IV_type = "circle"
        self.IV_size["radius"] = 1

    def setRadius(self, radius):
        return_msg = "Circle:setRadius: "
        debug_data = []
        success = RC.failed

        ## input validation

        if type(radius) is not float:
            return_msg += "input radius is not of type `float`"
        else:
            self.IV_size["radius"] = radius
            success = RC.success
            return_msg += "radius successfully set to %f" % radius

        ##</end> input validation

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}
    
    def getRadius(self):
        return_msg = "Circle:getRadius: "
        debug_data = []
        success = RC.success

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "radius": self.IV_size["radius"]}

    def calculateArea(self):
        return_msg = "Circle:calculateArea: "
        debug_data = []
        success = RC.success

        area = math.pi * self.IV_size["radius"] ** 2

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

class Square(Shape):

    def __init__(self):
        super().__init__()
        self.IV_type = "square"
        self.IV_size["length"] = 1
    
    def setLength(self, length):
        return_msg = "Square:setLength: "
        debug_data = []
        success = RC.failed

        ## input validation

        if type(length) is not float:
            return_msg += "input length is not of type `float`"
        else:
            self.IV_size["length"] = length
            success = RC.success
            return_msg += "length successfully set to %f" % length

        ##</end> input validation

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def getLength(self):
        return_msg = "Square:getLength: "
        debug_data = []
        success = RC.success

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "length": self.IV_size["length"]}

    def calculateArea(self):
        return_msg = "Square:calculateArea: "
        debug_data = []
        success = RC.success

        area = self.IV_size["length"] ** 2

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

class Rectangle(Shape):

    def __init__(self):
        super().__init__()
        self.IV_type = "rectangle"
        self.IV_size["width"] = 1
        self.IV_size["height"] = 1

    def setWidth(self, width):
        return_msg = "Rectangle:calculateArea: "
        debug_data = []
        success = RC.failed

        ## input validation

        if type(width) is not float:
            return_msg += "input width is not of type `float`"
        else:
            self.IV_size["width"] = width
            success = RC.success
            return_msg += "width successfully set to %f" % width

        ##</end> input validation

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def getWidth(self):
        return_msg = "Rectangle:getWidth: "
        debug_data = []
        success = RC.success

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "width": self.IV_size["width"]}

    def setHeight(self, height):
        return_msg = "Rectangle:setHeight: "
        debug_data = []
        success = RC.failed

        ## input validation

        if type(height) is not float:
            return_msg += "input height is not of type `float`"
        else:
            self.IV_size["height"] = height
            success = RC.success
            return_msg += "height successfully set to %f" % height

        ##</end> input validation

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def getHeight(self):
        return_msg = "Rectangle:getHeight: "
        debug_data = []
        success = RC.success

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "height": self.IV_size["height"]}

    def calculateArea(self):
        return_msg = "Rectangle:calculateArea: "
        debug_data = []
        success = RC.success

        area = self.IV_size["width"] * self.IV_size["height"]

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

class ShapeManager:

    def getCircleArea(self, radius):
        return_msg = "ShapeManager:getCircleArea: "
        debug_data = []
        success = RC.failed

        ## input validation

        if type(radius) is not float:
            return_msg += "input radius is not of type `float`"
        else:
            success = RC.success
            return_msg += "radius successfully validated"

        ##</end> input validation

        ## circle creation and validation

        circle = Circle()
        set_radius_result = circle.setRadius(radius)

        calculate_area_result = circle.calculateArea()

            ## return_msg passthrough

        return_msg += "\n" + set_radius_result[RDK.return_msg] + "\n" + calculate_area_result[RDK.return_msg]

            ##</end> return_msg passthrough

        success = success and set_radius_result[RDK.success] and calculate_area_result[RDK.success]

        ##</end>

        area = calculate_area_result["area"]

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

    def getSquareArea(self, length):
        return_msg = "ShapeManager:getSquareArea: "
        debug_data = []
        success = RC.failed

        ## input validation

        if type(length) is not float:
            return_msg += "input length is not of type `float`"
        else:
            success = RC.success
            return_msg += "length successfully validated"

        ##</end> input validation

        ## square creation and valdiation

        square = Square()
        set_length_result = square.setLength(length)

        calculate_area_result = square.calculateArea()

            ## return_msg passthrough

        return_msg += "\n" + set_length_result[RDK.return_msg] + "\n" + calculate_area_result[RDK.return_msg]

            ##</end> return_msg passthrough

        success = success and set_length_result[RDK.success] and calculate_area_result[RDK.success]

        ##</end> square creation and validation

        area = calculate_area_result["area"]

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

    def getRectangleArea(self, width, height):
        return_msg = "ShapeManager:getRectangleArea: "
        debug_data = []
        success = RC.failed

        ## input validation

        if type(width) is not float:
            return_msg += "input width is not of type `float`"
        else:
            success = RC.success
            return_msg += "width successfully validated"

        ##</end> input validation

        ## rectangle creation and validation

        rectangle = Rectangle()
        set_width_result = rectangle.setWidth(width)
        set_height_result = rectangle.setHeight(height)

        calculate_area_result = rectangle.calculateArea()

            ## return_msg passthrough

        return_msg += "\n" + set_width_result[RDK.return_msg] + "\n" + set_height_result[RDK.return_msg] + "\n" + calculate_area_result[RDK.return_msg]

            ##</end> return_msg passthrough

        success = success and set_width_result[RDK.success] and set_height_result[RDK.success] and calculate_area_result[RDK.success]

        ##</end> rectangle creation and validation

        area = calculate_area_result["area"]

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data, "area": area}

    def calcuateShapeAreasFromUserInput(self):
        return_msg = "ShapeManager:calcuateShapeAreasFromUserInput: "
        debug_data = []
        success = RC.failed

        shape = None

        ## input gathering and validation

        shape_type = input("Enter the type of shape or \"exit\" to exit: ")
        if shape_type == "circle":
            shape = Circle()
            return_msg += "shape type circle"

            radius = float(input("Enter radius of circle: "))

            set_radius_result = shape.setRadius(radius)

            success = set_radius_result[RDK.success]

            return_msg += "\n" + set_radius_result[RDK.return_msg]

        elif shape_type == "square":
            shape = Square()
            return_msg += "shape type square"

            length = float(input("Enter length of square: "))

            set_length_result = shape.setLength(length)
            
            success = set_length_result[RDK.success]

            return_msg += "\n" + set_length_result[RDK.return_msg]

        elif shape_type == "rectangle":
            shape = Rectangle()
            return_msg += "shape type rectangle"

            width = float(input("Enter width of rectangle: "))
            height = float(input("Enter height of rectangle: "))

            set_width_result = shape.setWidth(width)
            set_height_result = shape.setHeight(height)

            success = set_width_result[RDK.success] and set_height_result[RDK.success]

            return_msg += "\n" + set_width_result[RDK.return_msg] + "\n" + set_height_result[RDK.return_msg]

        elif shape_type in ("quit", "exit"):
            return_msg += "user exited function"
            return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

        else:
            return_msg += "shape type \"%s\"" % shape_type
            print("\"%s\" is not a valid shape" % shape_type)

        ##</end> input gathering

        ## area calculation

        if success:
            calculate_area_result = shape.calculateArea()

            success = calculate_area_result[RDK.success]

            return_msg += "\n" + calculate_area_result[RDK.return_msg]

            area = calculate_area_result["area"]

            print("Area of %s is %g" % (str(shape.getShapeType()["type"]), area))

        ##</end> area calculation

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

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