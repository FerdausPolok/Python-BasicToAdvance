"""
Printing tgwo separate print lines side by side using end keyword arg
"""
print("Ferdaus Zaman", end="")
print("Polok")

"""
Print auto space using ,
"""

print("Polok","Zholok","Kolok")

"""
Print Manual separating mark using sep 
"""

print("Nolok","Jholok", "Molok", sep="_")

#Scope

"""
Outside of the Function: Global Scope
Inside of the Function: Local Scope
-> We can use Global variable inside Local Scope but 
-> We can not use Local variable in Global Scope
"""

#Exception Handaling in Py using try and except keyword

def fun(x):
    try:
        return 100/x
    except:
        return 'There is a zero division error'

print(fun(0))





