def menu_display():
    print("")
    print('Menu')
    print('-'*13)
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()


decoded_pass = '' # Supposed to store the password longer term, so I moved my partner's variable up here - Sherif
while True:
    menu_display()
    option = input('Please enter an option: ')
    if option == '3':
        break
    elif option == '1':
        original_pass = input('Please enter your password to encode: ')
        list = [] 
        for i in range(len(original_pass)):
            list.append(int(original_pass[i]))
        for digit in list:
            digit += 3
            digit %= 10
            decoded_pass += str(digit)
        print('Your password has been encoded and stored!')
    elif option == '2': # Decoding program written by Sherif
        encoded_password = decoded_pass
        original_password = ""
        for digit in encoded_password:
            original_password += str((int(digit) - 3)%10)
        print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
