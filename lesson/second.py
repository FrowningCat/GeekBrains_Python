print("Create a list that contains numbers describing an increasing sequence. The order cannot be changed")

from random import choices

def get_list(n):
    return choices(range(n * 2), k = n)

def find_sub(ls):
    res = []
    for i in range(len(ls)):
        cur = ls[i]
        cur_ls = [cur]
        for k in range(i, len(ls)):
            if ls[k] > cur:
                cur_ls.append(ls[k])
                cur = ls[k]
        if len(cur_ls) > 1:
            res.append(cur_ls)
    return res

N = int(input("Enter a number: "))
ls = get_list(N)

print(ls)
print(find_sub(ls))