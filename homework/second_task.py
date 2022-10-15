print("For numbers ranging from 20 to N, find numbers that are multiples of 20 or 21")

x = int(input("Enter a number: "))

list = [i for i in range(20, x + 1) if i % 20 == 0 or i % 21 == 0]

print(f"A list of multiples of 20 or 21 in the range 20 - {x}: {list}")
