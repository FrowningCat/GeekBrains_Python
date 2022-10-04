x = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))

def trans(x):
    if x == 0:
        print(0)
    else:
        bit = []
        while x:
            bit.append(x % 2)
            x >>= 1
        print(bit[::-1])

trans(x)
