print('Create a list of length n, using the formula 3k +1, where k is from 1 to n')
n = int(input('Enter a number '))
ls = list()

for i in range(1, n + 1):
    ls.append(3 * i + 1)

print(ls)