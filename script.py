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


def process(data):
    result = []
    p = 1
    for x in data:
        if x!= 0:
            counter = 2
            for i in range(2,x):
                if x % i == 0:
                    counter += 1
            if counter == 2:
                p = p*x
            if x != 1:
                result.append(counter)
            else:
                result.append(1)
        else:
            result.append(0)
    if p == 1:
        result.append(0)
    else:
        result.append(p)
    return result
