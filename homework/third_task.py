print('Set a list of n numbers filled with the formula (1 + 1/n) ** n and display their sum on the screen')
n = int(input('Enter a number '))
ls = list()

for i in range(1, n + 1):
    ls.append(round((1 + 1 / i) ** i))

print(sum(ls))
print(ls)
