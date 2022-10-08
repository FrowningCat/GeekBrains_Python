print("Set the sequence of numbers. Write a program that outputs a list of non-repeating elements of the original sequence in the same order")

from random import randint

n = int(input("Enter the numbers separated by a space: "))
lis =[]
new_lis = []

for i in range(n):
    lis.append(randint(1, 10))

print(f"Source list: {lis}")

for i in lis:
    if i not in new_lis:
        new_lis.append(i)

print(f"A list of non-repeating elements: {new_lis}")
