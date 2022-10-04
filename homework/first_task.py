import random

print("Set a list consisting of arbitrary numbers, the number is set by the user."
      "Write a program that will find the sum of the list items standing in odd positions (not indexes)")

num = int(input("Enter a number "))
nums_list = list(range(100))
random.shuffle(nums_list)

print(nums_list[:num])

def magic(len, nums):
    sum = 0
    for i in range(len):
        if i % 2 == 0:
            sum += nums[i]
    print(f"The sum of the list items in odd positions (on indexes) is equal to {sum}")

magic(num, nums_list)
