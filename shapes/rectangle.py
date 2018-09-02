'''
Author: Nick Russo
File: rectangle.py
Purpose: Definition of the rectangle object, inherited from
the abstract class Shape.
'''

from shapes.shape import Shape

class Rectangle(Shape):
    '''
    Represents a Rectangbel shape, and contains a length value
    and width value.
    '''
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        '''
        Compute the area using the formula length * width
        '''
        return self.length * self.width

    def perimeter(self):
        '''
        Compute the perimeter using the formula (length + width) * 2
        '''
        return (self.length + self.width) * 2

    def is_square(self):
        '''
        Determine if the rectangle is a square by comparing the length
        and width for equality. Note this method is specific to
        rectangles and is not defined in the Shape class.
        '''
        return self.length == self.width
