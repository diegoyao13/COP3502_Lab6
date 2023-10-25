def menu_display():
    print("")
    print('Menu')
    print('-'*13)
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()


while True:
    menu_display()
    option = input('Please enter an option: ')
    if option == '3':
        break
    elif option == '1':
        original_pass = input('Please enter your password to encode: ')
        list = []
        decoded_pass = ''
        for i in range(len(original_pass)):
            list.append(int(original_pass[i]))
        for digit in list:
            digit += 3
            decoded_pass += str(digit)
        print('Your password has been encoded and stored!')
