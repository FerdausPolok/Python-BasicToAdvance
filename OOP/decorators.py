#decorators are an enique property of python

def outer(message):
    print('In the outer function')

    def inner():
        print('Calling the inner function')
        print(message)

    return inner

f = outer("Zaman")
f()

def decorator(original_fun):
    print("In er Decoration Function\n")

    def wrapper():
        print(f"Wrapper exicuted before {original_fun.__name__}()")

        if 10>5:
            print('Yes it is True')
        return original_fun()
    return wrapper

#how to use the decorator

def print_st():
    print("Print_sm is running")


#using decorator in one way
decoratied_f= decorator(print_st) #function k pass korle () chara korte hobe
decoratied_f()

#using decorator another way

@decorator
def print_st_new():
    print("Print_st_new is running")
print_st_new()


#non keyword arguments => f(1,2,3)
#keyword arguments => f(a=1, b=2 , c=3)

print("\n decorator 2 \n")

def decorator2(original_fun):
    print("\nIn er Decorator 2 Function\n")

    def wrapper(*args, **kwargs):
        print(f"Wrapper exicuted before {original_fun.__name__}()")
        if 10>5:
            print('Yes it is True')
        return original_fun(*args, **kwargs)
    return wrapper

@decorator2
def print_st_new_2(arg1, arg2):
    print(f"Printing argument 1 = {arg1} and Argument 2 = {arg2}")

print_st_new_2(1,2)