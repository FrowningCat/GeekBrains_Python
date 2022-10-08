print("Specify a string from a set of numbers. Write a program that will show a larger and smaller number")

def func(str):
    for index, num in enumerate(str):
        str[index] = num.strip('.,;:?!')
        if not str[index].replace("-", "").isdigit():
            return []
    return str


def min_sum(val):
    art = func(val)

    if art:
        return min(art, key=int), max(art, key=int)
    else:
        return []


print(min_sum(input().split()))
