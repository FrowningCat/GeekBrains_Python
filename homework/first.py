print("Write a program that removes all words containing 'abc' from the text. The text uses a space separator")

from random import sample

def list(num):
    array = []
    for i in range(num):
        str = sample('abc', 3)
        array.append("".join(str))
    return ", ".join(array)

all_list = list(int(input("Enter the number of words: ")))
lst = [i for i in all_list.split() if 'abc' not in i]

print(all_list)
print(f'Результат: {" ".join(lst)}')