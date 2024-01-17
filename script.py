def remove_even_digits(number):
    num_str = str(number)
    filtered_digits = [digit for digit in num_str if int(digit) % 2 != 0]
    result_number = int(''.join(filtered_digits))
    return result_number

def remove_odd_digits(number):
    num_str = str(number)
    filtered_digits = [digit for digit in num_str if int(digit) % 2 == 0]
    result_number = int(''.join(filtered_digits))
    return result_number
