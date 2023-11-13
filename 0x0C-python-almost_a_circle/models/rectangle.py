#!/usr/bin/python3
""" define module"""
from models.base import Base


class Rectangle(Base):
    """define Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''prop'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_int('width', value, False)
        self.__width = value

    @property
    def height(self):
        '''prop'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_int('height', value, False)
        self.__height = value

    @property
    def x(self):
        '''prop'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_int('x', value)
        self.__x = value

    @property
    def y(self):
        '''prop'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_int('y', value)
        self.__y = value

    def validate_int(self, name, value, key=True):
        '''validate'''
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if key and value < 0:
            raise ValueError('{} must be >= 0'.format(name))
        elif not key and value <= 0:
            raise ValueError('{} must be > 0'.format(name))

    def area(self):
        '''area'''
        return self.__width * self.__height

    def display(self):
        '''desplay'''
        for i in range(self.__height):
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        '''str'''
        return '[Rectangle] ({}) {}/{} - {}/{}'.\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        '''update'''
        j = 1
        for i in args:
            if j == 1:
                self.id = i
            elif j == 2:
                self.__width = i
            elif j == 3:
                self.__height = i
            elif j == 4:
                self.__x = i
            elif j == 5:
                self.__y = i
            j += 1

        if args:
            pass
        else:
            for key, value in kwargs.items():
                if key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                elif key == 'id':
                    self.id = value

    def to_dictionary(self):
        '''dict'''
        dic = \
            {'id': self.id, 'width': self.width,
             'height': self.height, 'x': self.x, 'y': self.y}
        return dic
