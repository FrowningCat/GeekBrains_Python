print("Set a list of arbitrary real numbers, the number is set by the user."
      "Write a program that will find the difference between the maximum and minimum values of the fractional part of the elements")

lst = list(map(float, input("enter the numbers separated by a space:\n").split()))
min = 1
max = 0

for i in lst:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)

print("Array: ", lst, "\n" "Min: ", f"{min:0.2}", "\n" "Max: ", f"{max:0.2}", "\n" "Difference: ", f"{max-min:0.2}")