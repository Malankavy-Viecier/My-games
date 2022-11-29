from random import randint
w = 0 #Number of correct answer
for k in range(1, 21):
    x = randint(1, 10)
    y = randint(1, 10)
    print('What is', x, '*', y, '?')
    c = int(input('Your answer: '))
    z = x * y
    if z == c:
        print('Correct answer!')
        w = w + 1
    else:
        print('Wrong answer!')
print('Number of correct answer: ', w)
