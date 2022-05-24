#Printing from 0 to user given input all numbers using all lopps in python

#while
num = int(input("Please enter a Int number: "))
i=0
while(num>=i):
    print(i)
    i+=1

"""for

range() has three perameter - start, stop, step size
range(3) -> start from 0 end at 3-1 step 1 -> 0,1,2
range(1,3) -> start from 1 end at 3-1 step 1 ->1,2
range(2,11,2) -> start from 2 end at 11-1 step 2 ->2,4,6,8,10"""

for i in range(num+1):
    print(i)

for i in range (2,11,2):
    print(i)

for i in range (2,-11,-2):
    print(i)





