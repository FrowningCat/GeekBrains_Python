print('Write a program that takes the coordinates of two points as input and finds the distance between them in 2D space')
x1 = int(input('Enter x1 '))
y1 = int(input('Enter y1 '))
x2 = int(input('Enter x2 '))
y2 = int(input('Enter y2 '))

print(round(((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5), 3))