def regi():
    info = []
    phone_number = ''
    valid = False

    last_name = input('Enter your last name: ')
    first_name = input('Enter a name: ')

    while not valid:
        try:
            phone_number = input('Enter the phone number, it should start with 8: ')
            if len(phone_number) != 11:
                print('The phone number must have 11 digits: ')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('The phone number should consist only of digits.')

    description = input('Enter a description: ')

    info.append(first_name)
    info.append(last_name)
    info.append(phone_number)
    info.append(description)

    file = 'date.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'User: {info}\n')
