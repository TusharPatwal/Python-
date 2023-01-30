def bin_to_decimal(bin_num):
    decimal_num = 0
    for digit in bin_num:
        decimal_num = decimal_num * 2 + int(digit)
    return decimal_num

print(bin_to_decimal('1010'))  # prints 10
print(bin_to_decimal('110101'))  # prints 53
print(bin_to_decimal('1'))  # prints 1
print(bin_to_decimal('0'))  