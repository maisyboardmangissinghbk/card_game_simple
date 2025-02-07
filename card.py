"""
## card game for homework ##

first check colors:
 #  red beats black
 #  yellow beats red
 #  black beats yellow
then check values

"""

# imports
from random import shuffle

# set up vars and consts
deck = []
playerOne = []
playerTwo = []
colors= ['R', 'B', 'Y'] # do not edit this!
validUsers = [ 'FOO', 'BAR', 'MAISY']
enteredUsername = ''
SUIT_SIZE = 10


# card class
class Card:

    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __repr__(self):
        # used identically to __str__ in this
        return f'{self.color}{self.value}'

    def __eq__(self, other):
        # this isn't really needed but it's easy to implement
        return (self.color == other.color) and (self.value == other.value)

    def __lt__(self, other):
        if isinstance(other, Card):
            # see multiline at the beginning
            if self.color == other.color:
                if self.value < other.value:
                    return True
                else:
                    return  False
            else:
                if self.color == 'R':
                    if other.color == 'B':
                        return False
                    else:
                        return True
                elif self.color == 'Y':
                    if other.color == 'B':
                        return True
                    else:
                        return False
                else:
                    if other.color == 'Y':
                        return False
                    else:
                        return True

try:
    file = open('scores.txt', 'r')
    scores = [line.strip() for line in file.readlines()]
    scores.sort()
    scores.reverse()
    topScores = scores[:4]
finally:
    file.close()
if len(topScores) > 1:
    print(f'\nTop {len(topScores)} scores:')

for score in topScores:
    print(score)

while enteredUsername.upper() not in validUsers:
    enteredUsername = input('Enter player 1 username:  ')
    if enteredUsername.upper() not in validUsers:
        print('Invalid, try again!')
print(f'\nWelcome, {enteredUsername.title()}')
usernameOne = enteredUsername.title()
validUsers.remove(enteredUsername.upper()) # so one doesn't go against themselves

while enteredUsername.upper() not in validUsers:
    enteredUsername = input('\nEnter player 2 username:  ')
    if enteredUsername.upper() not in validUsers:
        print('Invalid, try again!')
print(f'\nWelcome, {enteredUsername.title()}')
usernameTwo = enteredUsername.title()
validUsers.remove(enteredUsername.upper())

# generate deck
for color in colors:
    for value in range(1, SUIT_SIZE+1):
        deck.append(f'{color}{value}')
shuffle(deck)
print('\nDeck Shuffled!')

while len(deck) != 0:
    # draw cards
    input(f'{usernameOne}, press [Return] to draw next card: ')
    drawnPlayerOneStr = deck[0]
    print(f'{usernameOne} drew {drawnPlayerOneStr}')
    input(f'{usernameTwo}, press [Return] to draw next card: ')
    drawnPlayerTwoStr = deck[1]
    print(f'{usernameTwo} drew {drawnPlayerTwoStr}')
    drawnPlayerOne = Card(drawnPlayerOneStr[0], drawnPlayerOneStr[1:])
    drawnPlayerTwo = Card(drawnPlayerTwoStr[0], drawnPlayerTwoStr[1:])
    deck.pop(0)
    deck.pop(0)

    # add cards to winner deck
    if drawnPlayerOne > drawnPlayerTwo:
        playerOne.append(drawnPlayerOne)
        playerOne.append(drawnPlayerTwo)
        print(f'{usernameOne} wins! - {len(deck)} cards left')
    else:
        playerTwo.append(drawnPlayerTwo)
        playerTwo.append(drawnPlayerOne)
        print(f'{usernameTwo} wins! - {len(deck)} cards left')
    input('\nPress [Return] to continue:  ')

    del drawnPlayerOne
    del drawnPlayerTwo

# display winner
if len(playerOne) > len(playerTwo):
    print(f'{usernameOne} won by {len(playerOne)-len(playerTwo)}')
    score = len(playerOne)
    winner = 1
else:
    print(f'{usernameTwo} won by {len(playerTwo)-len(playerOne)}')
    score = len(playerTwo)
    winner = 2

if len(str(score)) != 2:
    score = int('0' + str(score))

# save to disk
try:
    file = open('scores.txt', 'a')
    if winner == 1:
        scores = file.write(f'{score} {usernameOne}\n')
    else:
        scores = file.write(f'{score} {usernameTwo}\n')
except:
    print('file error')
finally:
    file.close()
