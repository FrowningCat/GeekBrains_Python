print('Write a program that accepts 2 numbers as input. Specify a list of N elements filled with numbers from the'
      ' interval [-N, N]. Find the product of the elements at the specified positions (not indexes)')
n = int(input('Enter number of elements '))
x = int(input('Enter position one ')) -1
y = int(input('Enter position two ')) -1
ls = list()
sum = 0

for i in range(-n, n + 1):
    ls.append(i)

sum = ls[x] * ls[y]
print(ls)
print('Position one * position two = ', sum)
