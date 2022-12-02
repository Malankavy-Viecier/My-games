from random import randint
import time

n = randint(15, 25)

print('Total of', n, 'items')

for i in range(n):
    print('O ', end = '')

k = randint(3, 5)
print()
print('You can take no more than', k, 'items.')

time.sleep(3)

succ = randint(1, 2)
if succ == 1:
    print('Computer starts!')
else:
    print('Your start!')

time.sleep(3)

while True:
    if succ == 1:
        if n >= k:
            took1 = randint(1, k)
        else: #n < k
            took1 = randint(1, n)
        time.sleep(3)
        print('Computer:', took1)
        n = n - took1   
    else:
        took2 = int(input('How many items will you take? '))
        while took2 > k or took2 <= 0:
            print('You put the wrong number! Please try again!')
            took2 = int(input('How many items will you take? '))
        n = n - took2
    if n == 0:
            if succ == 2:
                print('You took the last item. The computer won!')
                break
            else:
                print('The computer took the last item. You won!')
                break
    else:
        print('How many items are left?', n)
        for i in range(n):
            print('O ', end = '')
        print()
        if succ == 1:
            succ = 2
        else:
            succ = 1
        
    
