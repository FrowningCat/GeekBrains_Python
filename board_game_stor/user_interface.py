import sys


def inter():
    print('\033[32mIf you want to add a game to the list of available, press 1')
    print('\033[32mIf you want to see the list of available games, press 2')
    print('\033[32mIf you want to add a game to the list of soon, press 3')
    print('\033[32mIf you want to see a list of games that will appear soon, press 4')
    print('\033[32mIf you want to register a user, press 5')
    print('\033[32mIf you want to see the list of users, press 6\n')

    n = int(input('\033[38mEnter the number: '))

    if n < 1 or n > 6:
        sys.exit('Incorrect number entered!')

    return n
