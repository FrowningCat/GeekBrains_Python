print("A list of numbers is presented. It is necessary to output the elements of the source list "
      "whose values are greater than the previous element")

import random

n = int(input("Enter a number: "))
rand_list = []
result_list = []

for i in range(n):
      rand_list.append(random.randint(1, 101))

for i in range(1, len(rand_list)):
      if rand_list[i] > rand_list[i - 1]:
            (result_list.append(rand_list[i]))

print("Source list: ", rand_list)
print("A list whose elements are larger than the previous one: ", result_list)
