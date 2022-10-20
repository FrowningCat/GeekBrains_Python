from user_interface import a, b

n = 0


def div(x, y):
    global n
    n = x / y
    print(n)


def writing_txt(z):
    file = 'result.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'result: {z}\n')


div(a, b)
writing_txt(n)
