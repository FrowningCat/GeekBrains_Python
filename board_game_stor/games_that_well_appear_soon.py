def soon():
    file = 'soon.txt'
    f = open(file, 'r', encoding='utf-8')
    print(*f)


soon()
