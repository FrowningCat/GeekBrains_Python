print("Set the number. Make a list of Fibonacci numbers, including for negative indexes")

import sys

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def neg_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2


list = []

leng = int(input('Enter the length of the array: '))
if leng < 1:
    sys.exit('Incorrect number entered')

for e in range(1, leng + 1):
    list.append(fib(e))
print(list, "\n")

for e in range(0, leng + 1):
    list.insert(0, neg_fib(e))
print(f"Negafibonacci: {list}")
