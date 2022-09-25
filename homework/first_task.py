print('Write a program that takes as input a number representing the day of the week and checks if that day is a holiday')
a = int(input('Enter number '))

if (a > 0) and (a < 6):
    print('No')
elif (a == 6) or (a == 7):
    print('Yus')
else:
    print('You entered the wrong number')