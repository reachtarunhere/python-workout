def hex_char_to_int(c):
    if ord('a') <= ord(c) <= ord('f'):
        return ord(c) - ord('a') + 10
    elif ord('0') <= ord(c) <= ord('9'):
        return ord(c) - ord('0')


def hex_output():
    hex_str = input("enter hexadecimal number ").lower()
    integer = 0
    for position, digit in enumerate(reversed(hex_str)):
        digit_int = hex_char_to_int(digit)
        if digit_int:
            integer += digit_int * 16 ** position
    print(integer)


hex_output()
