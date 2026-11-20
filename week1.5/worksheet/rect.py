# Worksheet 1.5: Rectangle class

class Rectangle:
    """rectangle class"""
    def __init__(self, width, height):
        """sets up width and height"""
        # check types
        if type(width) != int:
            raise TypeError("width not int")
        if type(height) != int:
            raise TypeError("height not int")
        # check values
        if width <= 0:
            raise ValueError("width too small")
        if height <= 0:
            raise ValueError("height too small")
        self.width=width
        self.height=height

    def is_square(self):
        """checks if square"""
        if self.width == self.height:
            return True
        else:
            return False

    def area(self):
        """calculates area"""
        a = self.width * self.height
        return a

    def perimeter(self):
        """calculates perimiter"""
        p = self.width + self.width + self.height + self.height
        return p
