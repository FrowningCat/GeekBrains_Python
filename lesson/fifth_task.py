print('Checks if a number is a multiple of 5, 10 or 15, but not 30')
a = int(input('Enter number '))

if (a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and a % 30 != 0:
    print('yus')
else:
    print('no')