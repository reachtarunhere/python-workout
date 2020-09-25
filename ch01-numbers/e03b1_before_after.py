def before_after(num, before, after):
    num_str = str(num)
    decimal_index = num_str.find('.')
    before_digits = num_str[decimal_index-before:decimal_index]
    after_digits = num_str[decimal_index:decimal_index+after+1]
    return float(before_digits+after_digits)


print(before_after(1234.5678, 2, 3))
