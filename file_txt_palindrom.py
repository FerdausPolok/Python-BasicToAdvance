"""
f = open('plaindrom.txt', 'w+')
f.write("HelleH")
f.close()

"""



f = open('plaindrom.txt', 'r+')
check= list(f.read())

print(check)
stat = 0;
end = len(check)-1
flag = False
while stat <= end:
    if check[stat] == check[end]:
        if stat==end or  end-stat ==1 :
            flag = True
    else:
        break

    stat+=1
    end-=1

if flag == True:
    print("Pali")
else:
    print("Not Pali")


