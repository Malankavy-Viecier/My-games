from random import randint
import time

player1 = input('Name1: ')
player2 = input('Name2: ')

n = 7

w1 = 0 #Win player1
w2 = 0 #Win player2
dr = 0 #Number of draws

for k in range(n):
    trump_suit = randint(1, 4) #Set the trump suit
    if trump_suit == 1:
        print('Set the trump suit: spades')
    elif trump_suit == 2:
        print('Set the trump suit: clubs')
    elif trump_suit == 3:
        print('Set the trump suit: diamonds')
    else:
        print('Set the trump suit: hearts')
        
    suit_number_1 = randint(1, 4)
    card_value_1 = randint(6, 14)

    if suit_number_1 == 1:
        suit = 'spades'
    elif suit_number_1 == 2:
        suit = 'clubs'
    elif suit_number_1 == 3:
        suit = 'diamonds'
    else:
        suit = 'hearts'

    if card_value_1 == 6:
        value = 'six'
    elif card_value_1 == 7:
        value = 'seven'
    elif card_value_1 == 8:
        value = 'eight'
    elif card_value_1 == 9:
        value = 'nine'
    elif card_value_1 == 10:
        value = 'ten'
    elif card_value_1 == 12:
        value = 'queen'
    elif card_value_1 == 13:
        value = 'king'
    else:
        value = 'ace'

    time.sleep(3)
    print(player1, ' - ', 'the', value, 'of', suit)

    suit_number_2 = randint(1, 4)
    card_value_2 = randint(6, 14)

    if suit_number_2 == 1:
        suit = 'spades'
    elif suit_number_2 == 2:
        suit = 'clubs'
    elif suit_number_2 == 3:
        suit = 'diamonds'
    else:
        suit = 'hearts'

    if card_value_2 == 6:
        value = 'six'
    elif card_value_2 == 7:
        value = 'seven'
    elif card_value_2 == 8:
        value = 'eight'
    elif card_value_2 == 9:
        value = 'nine'
    elif card_value_2 == 10:
        value = 'ten'
    elif card_value_2 == 12:
        value = 'queen'
    elif card_value_2 == 13:
        value = 'king'
    else:
        value = 'ace'

    time.sleep(3)
    print(player2, ' - ', 'the', value, 'of', suit)

    if trump_suit == suit_number_1 and trump_suit != suit_number_2:
       print('Wins', player1)
       w1 = w1 + 1
    elif trump_suit == suit_number_2 and trump_suit != suit_number_1:
       print('Wins', player2)
       w2 = w2 + 1
    elif trump_suit == suit_number_1 and trump_suit == suit_number_2:
        if card_value_1 > card_value_2:
            print('Wins', player1)
            w1 = w1 + 1
        elif card_value_2 > card_value_1:
            print('Wins', player2)
            w2 = w2 + 1
        else:
            print('Draw!')
            dr = dr + 1
    else:
        if suit_number_1 > suit_number_2:
            print('Wins', player1)
            w1 = w1 + 1
        elif suit_number_2 > suit_number_1:
            print('Wins', player2)
            w2 = w2 + 1
        else:
            if card_value_1 > card_value_2:
                print('Wins', player1)
                w1 = w1 + 1
            elif card_value_2 > card_value_1:
                print('Wins', player2)
                w2 = w2 + 1
            else:
                print('Draw!')
                dr = dr + 1

#Outcome of the game
print(player1, 'Wins', w1, 'times')
print(player2, 'Wins', w2, 'times')
print('Number of draws:', dr)
