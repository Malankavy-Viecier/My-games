from random import randint
import time

n = 7 #Q&A

player1 = input('Name1: ')
player2 = input('Name2: ')

w1 = 0 #Win player1
w2 = 0 #Win player2
dr = 0 #Number of draws

for k in range(n):
    print('Throws the dice', player1)
    time.sleep(3)
    n1 = randint(1, 6)
    print('Number:', n1)

    print('Throws the dice', player2)
    time.sleep(3)
    n2 = randint(1, 6)
    print('Number:', n2)

    if n1 > n2:
        w1 = w1 + 1
    elif n1 < n2:
        w2 = w2 + 1
    else:
        dr = dr + 1

#Outcome of the game
print(player1, 'Wins', w1, 'times')
print(player2, 'Wins', w2, 'times')
print('Number of draws:', dr)
