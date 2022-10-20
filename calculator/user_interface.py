import sys


def output_date():
    global a, b

    a = int(input('Enter the first whole number: '))
    b = int(input('Enter the second whole number: '))

    return a, b


def out_green(text):
    print('\033[32m{}' .format(text))


def out_white(text):
    print('\033[38m{}' .format(text))


a = 0
b = 0
n = 0

output_date()

out_green(f'\nIf you want to add up the numbers, press 1')
out_green(f'If you want to subtract {b} from {a}, press 2')
out_green(f'If you want to multiply the numbers, press 3')
out_green(f'If you want to divide the {a} by the {b}, press 4')
out_green(f'If you want to raise the {a} to the power of the {b}, press 5')
out_green(f'If you want to find {b} percentages from the number {a}, press 6')

out_white('')
n = int(input('Enter the number: '))

if n < 1 or n > 6:
    sys.exit('Incorrect number entered!')
