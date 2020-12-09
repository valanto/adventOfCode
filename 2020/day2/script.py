import re

file = open("./input.txt", "r")
valid_password_counter_1 = 0
for line in file:
    match = re.match(r"^(\d+)-(\d+)\s+([A-Za-z]):\s+([A-Za-z]+)$", line)
    min = int(match.group(1))
    max = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)

    number_of_times_letter_appears = password.count(letter)
    if number_of_times_letter_appears >= min and number_of_times_letter_appears <= max:
        valid_password_counter_1 += 1


print("part1: {0}".format(valid_password_counter_1))
file.close()

file = open("./input.txt", "r")
valid_password_counter_2 = 0
for line in file:
    match = re.match(r"^(\d+)-(\d+)\s+([A-Za-z]):\s+([A-Za-z]+)$", line)
    position1 = int(match.group(1)) - 1
    position2 = int(match.group(2)) - 1
    letter = match.group(3)
    password = match.group(4)

    position1_character = password[position1] if len(password) > position1 else None
    position2_character = password[position2] if len(password) > position2 else None
    if (position1_character == letter and position2_character != letter) or (
        position1_character != letter and position2_character == letter
    ):
        valid_password_counter_2 += 1


print("part2: {0}".format(valid_password_counter_2))
file.close()