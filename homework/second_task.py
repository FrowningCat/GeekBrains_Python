print("Set a list consisting of arbitrary numbers, the number is set by the user."
      "Write a program that will find the sum of the list items standing in odd positions (not indexes)")

def sum(lst):
    for i in range((len(lst) + 1) // 2):
        new_lst = [lst[i] * lst[len(lst) - i - 1]]
        print(new_lst)

lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum(lst)
