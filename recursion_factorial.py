#iteratively
def factorial(num):
    fac = 1;
    if num==1:
        return 1
    elif num==0:
        return 0
    else:
        result = 1
        for i in range (2, num+1):
            result = result*i
        return result
print(factorial(5))

#recurssion

