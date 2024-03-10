def binary_to_decimal(binary: str):
    sum = 0
    current_index = 7
    for digit in binary:
        if int(digit) == 1:
            sum = sum + (2 ** current_index)
        current_index = current_index - 1
    return sum


def decimal_to_binary(number: int):
    binary = ""
    for place in range(7, -1, -1):
        if number >= (2 ** place):
            binary = binary + "1"
            number = number - (2 ** place)
        else:
            binary = binary + "0"
    return binary


def negative_decimal_to_binary(number: int):
    number = abs(number)
    binary_representation = decimal_to_binary(number)
    binary_in_negative = ""
    for digit in binary_representation:
        if digit == '1':
            binary_in_negative = binary_in_negative + '0'
        else:
            binary_in_negative = binary_in_negative + '1'
    binary_in_negative = list(binary_in_negative)
    added_1 = False
    index = 0
    while (not added_1) and (index <= 7):
        remember_1 = False
        current_bit = binary_in_negative[7 - index]
        if current_bit == '1':
            binary_in_negative[7 - index] = '0'
            remember_1 = True

        elif current_bit == '0' and not remember_1:
            binary_in_negative[7 - index] = '1'
            added_1 = True

        if current_bit == '0' and remember_1:
            binary_in_negative[7 - index] = '1'
            added_1 = False

        index = index + 1
    binary_in_negative = "".join(binary_in_negative)
    return binary_in_negative


print(negative_decimal_to_binary(-100))