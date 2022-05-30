#Count the number of time a letter in a sting

text = "this is a simple text to TEST the code"
letters= {}

for i in text:
    letters.setdefault(i, 0)
    letters[i]= letters[i]+1

import pprint as pp #sorted wise print
pp.pprint(letters)

#Password simulation

password_bank={
    'Sam': 1212,
    'Smith': 5244,
    'Rohim': 5241
}
matched = False
x = 0 #loop control variable

while x< 5:
    name = input("Enter your name: ")
    if name in password_bank.keys():
        for i in range(0,3):
            password= int(input("Enter you Password: "))
            if password in password_bank.values():
                matched= True
                print('Access Granted')
                break
            else:
                print("Wrong password. You have", 2-i, " Tries left! ")
    else:
        print("There is no such username in bank")
    x=x+1
    print(x)

    if matched:
        break




