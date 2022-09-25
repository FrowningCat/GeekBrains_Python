print('Write a program that takes as input the coordinates of a point (X and Y), with X ≠ 0 and Y ≠ 0,'
      'and outputs the quarter number of the plane in which this point is located (or on which axis it is located)')
a = int(input('Enter the first number '))
b = int(input('Enter the second number '))

if a > 0 and b > 0:
    print(1)
elif a > 0 and b < 0:
    print(4)
elif a < 0 and b > 0:
    print(2)
elif a < 0 and b < 0:
    print(3)
else:
    print('0 cannot be entered')