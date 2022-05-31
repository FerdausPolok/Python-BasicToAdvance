#sum from 1 to num

def sum(num):
    result = 0
    for i in range (1, num+1):
        result = result + i
    return result

print(sum(10))

def sum2(num):
    if num == 1:
        return 1
    return num + sum2(num-1)

print(sum2(10))

#List Reverse

def reverse(lst):
    newlst=[]
    x = len(lst)-1
    for i in range (0,len(lst)):
        newlst.append(lst[x])
        x= x-1
    return newlst
print(reverse([10,45,12,0,8.2]))

def reverse2(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]]+ reverse2(lst[:-1])
print(reverse2([10,45,12,0,8.2]))

def fibo(num):
    if num == 0:
        return [0]
    elif num == 1:
        return [1]

    else:
        f = 0
        s = 1
        result = [0, 1]
        for i in range(0, num-1):
            t = f + s
            result.append(t)
            f=s
            s=t
        return result

print(fibo(10))

def fibo2(num):
    if num<=1:
        return num
    return fibo2(num-1) + fibo2(num-2)

print(fibo2(10))


