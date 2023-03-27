
def password_encoder(data):
    encoded_password = ''
    for i in data:
        a = str((int(i)+3) % 10)
        encoded_password = encoded_password + a
    return encoded_password

if __name__ == '__main__':
    print("Menu")
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

    option = int(input('Please enter an option: '))

    if option == 1:
        password = input('Please enter your password: ')
        encoded_password = password_encoder(password)
        print(encoded_password)



