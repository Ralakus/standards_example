
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
        IV_type = ""
        IV_colour = ""
        IV_size = {}

    def setColour(self, colour):
        return_msg = "Shape:setColour: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def getColour(self):
        return_msg = "Shape:getColour: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"


        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def setShapeType(self, shape_type):
        return_msg = "Shape:setShapeType: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}
    
    def getShapeType(self):
        return_msg = "Shape:getShapeType: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def calculateArea(self):
        return_msg = "Shape:calculateArea: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

class Circle(Shape):

    def setRadius(self, radius):
        return_msg = "Circle:setRadius: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}
    
    def getRadius(self):
        return_msg = "Circle:getRadius: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def calculateArea(self):
        return_msg = "Circle:calculateArea: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

class Square(Shape):
    
    def setLength(self, length):
        return_msg = "Square:setLength: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def getLength(self):
        return_msg = "Square:getLength: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def calculateArea(self):
        return_msg = "Square:calculateArea: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

class Rectangle(Shape):

    def setWidth(self, width):
        return_msg = "Rectangle:calculateArea: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def getWidth(self):
        return_msg = "Rectangle:getWidth: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def setHeight(self, height):
        return_msg = "Rectangle:setHeight: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def getHeight(self):
        return_msg = "Rectangle:getHeight: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def calculateArea(self):
        return_msg = "Rectangle:calculateArea: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

class ShapeManager:

    def getCircleArea(self, radius):
        return_msg = "ShapeManager:getCircleArea: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def getSquareArea(self, length):
        return_msg = "ShapeManager:getSquareArea: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def getRectangleArea(self, width, height):
        return_msg = "ShapeManager:getRectangleArea: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    def calcuateShapeAreasFromUserInput(self):
        return_msg = "ShapeManager:calcuateShapeAreasFromUserInput: "
        debug_data = []
        success = RC.failed

        return_msg += "not implemented yet"

        return {RDK.success: success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}