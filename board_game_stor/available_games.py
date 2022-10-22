def available():
    file = 'available.txt'
    f = open(file, 'r', encoding='utf-8')
    print(*f)
