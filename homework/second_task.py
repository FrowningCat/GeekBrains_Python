print('Write a program that accepts the number N as input and outputs a set of products of numbers from 1 to N')
n = int(input('Enter a number '))
ls = list()
x = 1
y = 1

for i in range(1, n + 1):
    y = i * y
    ls.append(x * y)
    x = ++x

print(ls)
