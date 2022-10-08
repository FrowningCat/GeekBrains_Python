print("Set the natural number N. Write a program that will make a list of prime factors of the number N")

import sys

num = int(input("Enter a number: "))
i = 2
lis = []
pri = num

if num == 1:
    print(f"There is only one prime multiplier: {1}")
    sys.exit()
elif num < 1:
    sys.exit("Invalid number")

while i <= num:
    if num % i == 0:
        lis.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Prime factors of a number {pri}: {lis}")
