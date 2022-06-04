
class Point2D:
    def __init__(self, x, y): #this is one of python's magic method
        self.x= x
        self.y= y

    def __repr__(self):  #programmer purpose to know about object/ instance
        return f"Point2D({self.x, self.y})"

    def __str__(self): #general purpose to know about object/ instance
        return f"Class: Point2D, " \
               f"X: {self.x}, y: {self.y}"


p1 = Point2D(1, 2)
p2 = Point2D(2, 3)

#object print korar por useful demostration dekhano
print(p1) #str ta dekhachhe

#alada

print(repr(p2))
print(str(p1))

#__ <- these are called danders
