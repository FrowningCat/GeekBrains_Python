from user_interface import get_info as gi

info = gi()
def writing_scv():
    file = 'phone_book.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Surname: {info[0]}\nName: {info[1]}\nPhone number: {info[2]}\nDescription: {info[3]}\n\n')

def writing_txt():
    file = 'phone_book.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Surname: {info[0]}\nName: {info[1]}\nPhone number: {info[2]}\nDescription: {info[3]}\n\n')