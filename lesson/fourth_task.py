print('Shows the first number of a fraction')
a = float(input('Enter number '))

a = a * 10 % 10
if a != 0:
    print(int(a))
else:
    print('no')