def before_after(num, before, after):
    num_str = str(num)
    decimal_index = num_str.find('.')
    return float(num_str[decimal_index-before:decimal_index+after+1])


print(before_after(1234.5678, 2, 3))
