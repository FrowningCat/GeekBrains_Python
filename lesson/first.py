print("Create a list of N natural numbers from 0 to N, ordered in ascending order. Among which there is not one, "
      "find this number.")

from secrets import choice

def fill_list(num):
    array = [i for i in range(num + 1)]
    array.remove(choice(array))
    return array

def check(array):
    for i in range(1, len(array)):
        if array[i] - 1 != array[i - 1]:
            return array[i] - 1
    return -1

array = (fill_list(int(input("Enter a number: "))))

print(array)
print(check(array))
