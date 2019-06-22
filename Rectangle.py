class Rectangle:
    def __init__(self,wide=0, height=0):
        self.wide = wide
        self.height = height

    def __setattr__(self, key, value):
        if key == 'square':
            self.height = value
            self.wide = value
        else:
            super.__setattr__(key,value)

    def getArea(self):
        return self.wide * self.height

r = Rectangle(4, 5)
r.getArea()
r.square = 10
r.wide
r.height