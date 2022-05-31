#calculating the number of digit in a number

def digit(num):
    result = 1;
    while(num/10>=1):
        x = num/10
        result = result + 1
        num = x
    print(result)

digit(19457452454554)

def digit2(num):
    result =1
    if num<=1:
        return result
    return 1 + digit2(num//10)

print(digit2(19457452454554))


#exponantial x^y

def expo(x,y):
    if y==1:
        return x
    return x * expo(x, y-1)

print(expo(3,4))

