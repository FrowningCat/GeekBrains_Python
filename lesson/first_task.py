import random

print('Set a list of arbitrary length and determine if there is a number in it that the user entered')

def magic(count, find_num2):
    if count < 0:
        return 'Everything is bad'

    ls = random.sample(range(count * 2), count)
    print(ls)

    if find_num2 in ls:
        return 'Number yus'
    return 'Number no'


num1 = int(input('Enter the length of the array '))
num2 = int(input('Enter a number '))

print(magic(num1, num2))
