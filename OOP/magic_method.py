
class Point2D:
    def __init__(self, x, y): #this is one of python's magic method
        self.x= x
        self.y= y

    def __repr__(self):  #programmer purpose to know about object/ instance
        return f"Point2D({self.x, self.y})"

    def __str__(self): #general purpose to know about object/ instance
        return f"Class: Point2D, " \
               f"X: {self.x}, y: {self.y}"
    def __add__(self, other):
        if isinstance(self, other.__class__):
            return Point2D(self.x + other.x, self.y + other.y)
        else:
            return None
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.x == other.x and self.y == other.y
    def __nq__(self, other):
        if isinstance(self, other.__class__):
            return self.x != other.x or self.y != other.y
    def __lt__(self, other):
        if isinstance(self, other.__class__):
            return self.x < other.x or (self.y == other.x and self.y< other.y)
    def __hash__(self):
        return hash(self.x + self.y)





p1 = Point2D(1, 2)
p2 = Point2D(2, 3)

#object print korar por useful demostration dekhano
print(p1) #str ta dekhachhe

#alada

print(repr(p2))
print(str(p1))

#__ <- these are called danders

print("\n")
print("More Magic methods... \n\n")

print(f"Sum: {1+1}")
print(f"Sum: {int.__add__(1,1)}")

"""
print(f"Object sum: {p1 + p2}") 
will trow type error
to solve this we need to orver write the __add__ 
"""

print(f"Object sum: {p1 + p2}")
#same goes for subtract

print("\neq... \n")

print(p1 == p1 ) #first a none, overwrite korar por false
print(p1 is p1)

p6 = Point2D(1, 2)

print(p1 == p6 )
print(p1 is p6)

print("\nnot eq... \n")

print(p1 != p2 )
print(p1 != p6 )

print("\nless tan... \n")

print(p1 < p2 )
print(p1 < p6 )

print("\nhash... \n")

d= {}

d['polok'] = 100 #using hash to store
d['zaman'] = 200

print(d)
print(d['polok'])

point_Set = set()
point_dict = dict()

point_Set.add(p1) #hash need to be over write

print(point_Set)

point_dict[p1] = str(p1)

print(point_dict)




