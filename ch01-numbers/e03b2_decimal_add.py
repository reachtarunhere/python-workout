from decimal import Decimal


def decimal_add(num1, num2):
    return str(Decimal(num1) + Decimal(num2))


print(decimal_add('0.1', '0.2'))
