import os
import re


def get_numbers():
    numbers = []
    file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
    for line in file:
        number = int(line.strip())
        numbers.append(number)

    file.close()
    return numbers


def get_wrong_number(numbers):
    last25 = []
    for number in numbers:
        if len(last25) < 25:
            last25.append(number)
        else:
            match = False
            for i1, n1 in enumerate(last25):
                for i2, n2 in enumerate(last25):
                    if i1 != i2 and n1 + n2 == number:
                        match = True
                        break
                if match:
                    break
            if not match:
                return number
            else:
                last25.pop(0)
                last25.append(number)

    return None


def get_contiguous_numbers_for_invalid(numbers, invalid_number):
    contiguous = []
    sum = 0
    for number in numbers:
        sum += number
        contiguous.append(number)
        if len(contiguous) > 1 and sum == invalid_number:
            return contiguous
        elif sum > invalid_number:
            return get_contiguous_numbers_for_invalid(numbers[1:], invalid_number)

    return contiguous


numbers = get_numbers()
invalid_number = get_wrong_number(get_numbers())

print("part1: {0}".format(invalid_number))

contiguous = get_contiguous_numbers_for_invalid(numbers, invalid_number)
print("part2: {0}".format(min(contiguous) + max(contiguous)))
