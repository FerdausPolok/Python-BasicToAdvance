l=[]
def convert_number(num):
    if(num==0):
        return l
    digit=num%2
    l.append(digit)
    convert_number(2)
convert_number(6)
l.reverse()
for i in l:
    print(i,end="")