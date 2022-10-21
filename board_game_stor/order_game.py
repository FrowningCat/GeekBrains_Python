def order():
    info = []
    valid = False

    name = input('Enter the name of the game: ')
    date = ''
    description = input('Enter a description: ')

    while not valid:
        try:
            date = input('By what date do I need to make an order, the date must start from the day of the week, '
                         'through a point: ')
            if len(date) != 8:
                print('The date must have 8 digits: ')
            else:
                date = int(date)
                valid = True
        except:
            print('The date should consist only of digits.')

    info.append(name)
    info.append(date)
    info.append(description)

    file = 'soon.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'To order: {info}\n')


order()
