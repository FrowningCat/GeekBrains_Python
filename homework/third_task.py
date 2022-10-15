print("Write a function, arguments are the names of employees, returns a dictionary,"
      " keys are the first letters of names, values are lists containing names starting with the corresponding letter")

def key_name(names):
    res = {}
    for x in names:
        key = x[0].capitalize()
        if key not in res:
            res[key] = []
        res[key].append(x)
    return res

name = "Иван", "Мария", "Петр", "Илья"

print(key_name(name))
