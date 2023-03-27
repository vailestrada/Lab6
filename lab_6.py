
def password_encoder(data):
    encoded_password = ''
    for i in data:
        a = str((int(i)+3) % 10)
        encoded_password = encoded_password + a
    return encoded_password

def password_decoder(data):
    decoded_password = ''
    for i in data:
        digit = int(i)
        if digit < 3:
            digit += 10
        decoded_password += str(digit - 3)
    return decoded_password

if __name__ == '__main__':
    program_continue = True
    while program_continue:
        print("Menu")
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')

        option = int(input('Please enter an option: '))

        if option == 1:
            password = input('Please enter your password: ')
            encoded_password = password_encoder(password)
            print("Your password has been encoded and stored!\n")
        if option == 2:
            decoded_password = password_decoder(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
        if option == 3:
            program_continue = False


