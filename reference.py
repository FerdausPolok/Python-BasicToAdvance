#reference-> names pointing towards a certain piece of memory
#list reference ->
a = [1, 2, 3] #a is the list ref
b = a #b is new ref here not a new list. b is now pointing the same list as a was pointing

b[1] = '3.1416'
print(a)
print(b)


def changeList(list):
    list.append("ok")

x = [1,2,3]
changeList(x)

print(x) #x got change

#if we want x to be fresh than we should pass copy of x instead the main x

y = [2,3,4]
import copy as cp
z = cp.copy(y)

changeList(z)
print(y)

