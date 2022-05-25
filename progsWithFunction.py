#Fibo
def fibo(n):

    if n == 1:
        print("0")
    elif n == 2:
        print("0 1")
    else:
        x= 0
        y= 1
        print(x,y, end=" ")
        for i in range (2, n):
            z = x+y
            x=y
            y=z
            print(z, end=" ")


fibo(4)
