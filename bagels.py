import random;

NUM_DIGITS = 3
MAX_RETRIES = 20

def main():
    print('''
    bagels game :-
    I am thinking of a {}-digit number with no repeated digits.
     Try to guess what it is.
     When I say:    That means:
      Pico           One digit is correct but in the wrong position.
      Fermi          One digit is correct and in the right position.
      Bagels         No digit is correct.
    '''.format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum()
        print('I have thought of a number')
        print('You have {} retries to guess the number'.format(MAX_RETRIES))

        numGuesses=1
        while numGuesses <= MAX_RETRIES:
            guess=''
            while len(guess) !=NUM_DIGITS :
                print('Guess#{}-'.format(numGuesses))
                guess = input('> ')

            if guess == secretNum:
                print('You got it :')
                break

            clues = getClues(guess, secretNum)
            print(clues)

            numGuesses += 1


        if numGuesses > MAX_RETRIES:
            print('Exhausted no of retries')
            print('answer was {}'.format(secretNum))

        print('do you want to play more ?')
        if not input('> ').lower().startswith('y'):
            break

    print('Thanks for playing')


def getClues(guess, secretNum):
    clues = []

    for i in range(len(guess)):
        if (guess[i] == secretNum[i]):
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'

    clues.sort()
    return ' '.join(clues)


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

main()

