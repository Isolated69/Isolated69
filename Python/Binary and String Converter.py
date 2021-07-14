int_check = False
string_check = False
test = str()
bin_list = list()
byte_list = list()
output = str()
count = 0
print('''------------------\nBINARY CONVERTER\nCOMMANDS:\nq = quit\n_ = convert int to str\n------------------''')
while True:
    user_input = input('Enter text/binary[q]: ')
    if user_input == 'q':
        print('Quitting...')
        break
    test = user_input[0:9]
    try:
        int(test)
        int_check = True
        string_check = False
    except:
        string_check = True
        int_check = False
    if int_check:
        bin_list = user_input.split(' ')
        print(bin_list)
        for byte in bin_list:
            byte_int = int(byte, 2)
            byte_str = chr(byte_int)
            output += byte_str
        print(output)
        output = ''
    if string_check:
        if user_input.startswith('_'):
            user_input = user_input[1:]
        byte_arr = bytearray(user_input, 'utf8')
        for byte in byte_arr:
            bin_repr = bin(byte)
            byte_list.append(bin_repr)
            for letter in byte_list:
                output += letter
        print(output)
        output = ''
        byte_list = list()
