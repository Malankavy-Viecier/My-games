from random import randint
n_comp = randint(1, 100)
print('What number between 1 and 100 is computer chose?')
n = 0 #Number of attempts
while True:
    n = n + 1
    answer = int(input('Enter the number:'))
    if answer > n_comp:
        print('This number is less.')
    elif answer < n_comp:
        print('This number is greater.')
    else:
        print('Right! Number of attempts - ', n)
        break
