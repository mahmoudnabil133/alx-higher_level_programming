#!/usr/bin/python3
"""define a module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    '''define a class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''class constructor'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.validate_int('width', value, False)
        self.width = value
        self.validate_int('hieght', value, False)
        self.height = value

    def __str__(self):
        '''majic str function'''
        return '[Square] ({}) {}/{} - {}' .\
            format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        j = 1
        for i in args:
            if j == 1:
                self.id = i
            elif j == 2:
                self.width = i
                self.height = i
            elif j == 3:
                self.x = i
            elif j == 4:
                self.y = i
            j += 1

        if args:
            pass
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    self.width = value
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                elif key == 'id':
                    self.id = value

    def to_dictionary(self):
        dic = {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
        return dic
