def hex_output():
    hex_str = input("enter hexadecimal number")
    integer = 0
    for position, digit in enumerate(reversed(hex_str)):
        integer += int(digit, base=16) * 16 ** position
    print(integer)
