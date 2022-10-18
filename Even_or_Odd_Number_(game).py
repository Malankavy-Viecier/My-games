from random import randint

n = 13 #Q&A
correct = 0

for k in range(n):
    while True:
        answer = int(input('Even (Enter 2) or Odd (Enter 1)? '))
        if answer != 1 and answer != 2:
            print('You must enter 1 or 2. Please try again!')
        else:
            break
    n_comp = randint(1, 2)
    print('Random number:', n_comp)
    if answer == n_comp:
        correct = correct + 1

#Outcome of the game
if correct > n // 2:
    print('Score', correct, ':', n - correct, 'is in your favor. You win!', sep = ' ')
else:
    print('Score', n - correct, ':', correct, 'is in favor of computer. You lose!', sep = ' ')
