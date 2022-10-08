print("Calculate a number with a given precision d")

numb = float(input("Enter a number: "))
d = str(input("Enter a number: "))
n = len(str(d)) - 2
print(f'A number {numb} with a given precision {n} equally {round(numb, n)}')
