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


#Age guessing game

import random as rn

secretAge = rn.randint(1,10)
flag = False

def age_game(guessedAge, secret):
    if guessedAge<secret:
        return "Too low"
    elif guessedAge>secret:
        return "Too high"
    else:
        return "CORRECT!"

for i in range (1,6):
    print('Take a guess. You have ', 6-i, 'guesses left: ')
    guess= int(input())
    if age_game(guess, secretAge) == 'CORRECT!':
        print('You WON the GAME')
        flag= True
        break
if not flag:
    print("You LOST the GAME")


