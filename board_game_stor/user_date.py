def users():
    file = 'date.txt'
    f = open(file, 'r', encoding='utf-8')
    print(*f)


users()
