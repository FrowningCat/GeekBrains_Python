print('Write a program that accepts a real number as input and shows the sum of its digits')
num = int(input('Enter a number '))
sum = 0

while num > 0:
    i = num % 10
    num //= 10
    sum = sum + i

print('The sum of the numbers is =', sum)
