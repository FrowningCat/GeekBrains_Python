def get_info():
    info = []
    last_name = input('Enter your last name: ')
    info.append(last_name)
    first_name = input('Enter a name: ')
    info.append(first_name)
    phone_number = ''
    valid = False

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

    info.append(phone_number)
    description = input('Enter a description: ')
    info.append(description)

    return info