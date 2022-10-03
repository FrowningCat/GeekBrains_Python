print("Implement a list shuffling algorithm. Without the shuffle function from the random module")

from random import randrange

num = int(input("Enter a number "))
nums_list = list(range(num))
len_list = len(nums_list)

print(nums_list)

for i in range(len_list):
    n_1 = randrange(len_list)
    n_2 = randrange(len_list)
    nums_list[n_1], nums_list[n_2] = nums_list[n_2], nums_list[n_1]

print(nums_list)
