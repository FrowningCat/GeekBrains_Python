def add():
    info = []

    name = input('Enter the name of the game: ')
    nam = input('Enter the number of games: ')
    description = input('Enter a description: ')

    info.append(name)
    info.append(nam)
    info.append(description)

    file = 'available.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'In stock: {info}\n')


add()
