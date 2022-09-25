print('The program displays numbers from -N to N')
n = int(input('Enter number '))

if n < 0:
    n = n * (-1)
    print(list(range(-n, n + 1)))
else:
    print(*list(range(-n, n + 1)))