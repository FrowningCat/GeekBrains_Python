print('Write a program that, given a quarter number, shows the range of possible coordinates of points in that quarter (x and y)')
a = int(input('Enter number '))

if a == 1:
    print('x > 0, y > 0')
elif a == 2:
    print('x < 0, y > 0')
elif a == 3:
    print('x < 0, y < 0')
elif a == 4:
    print('x > 0, y < 0')
else:
    print('Invalid value entered')