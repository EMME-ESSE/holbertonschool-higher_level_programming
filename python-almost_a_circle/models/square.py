#!/usr/bin/python3
"""New class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Initialization of the class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return"""
        id = self.id
        x = self.x
        y = self.y
        w = self.width
        return ("[Square] ({}) {}/{} - {}".format(id, x, y, w))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """Update function"""
        if args:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
    
    def to_dictionary(self):
        """Dictionary"""
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
