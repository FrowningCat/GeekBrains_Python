from user_interface import a, b

n = 0


def expo(x, y):
    global n
    n = x ** y
    print(n)


def writing_txt(n):
    file = 'result.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'result: {n}\n')


expo(a, b)
writing_txt(n)
