import re
import os


def byr(value):
    return len(value) == 4 and int(value) >= 1920 and int(value) <= 2002


def iyr(value):
    return len(value) == 4 and int(value) >= 2010 and int(value) <= 2020


def eyr(value):
    return len(value) == 4 and int(value) >= 2020 and int(value) <= 2030


def hgt(value):
    match = re.match(r"^(\d+)(cm|in)$", value)
    return match != None and (
        (match.group(2) == "cm" and int(match.group(1)) >= 150 and int(match.group(1)) <= 193)
        or (match.group(2) == "in" and int(match.group(1)) >= 59 and int(match.group(1)) <= 76)
    )


def hcl(value):
    return re.match(r"^#[0-9a-f]{6}$", value) != None


def ecl(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def pid(value):
    return re.match(r"^\d{9}$", value) != None


MANDATORY_FIELDS = {"byr": byr, "iyr": iyr, "eyr": eyr, "hgt": hgt, "hcl": hcl, "ecl": ecl, "pid": pid}


def passport_scanner(validate):
    file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
    number_of_passports = 0
    number_of_invalid_passports = 0

    passports = []
    passport = dict()

    for line in file:
        if line.strip() == "":
            passport = dict()
            passports.append(passport)
        else:
            items = line.strip().split(" ")

            for item in items:
                (key, value) = item.split(":")
                passport[key] = value.strip()

    file.close()

    for pp in passports:
        missing = False
        invalid = False
        for field in MANDATORY_FIELDS.keys():
            if not (field in pp):
                missing = True
            elif not pp[field] or pp[field].strip() == "":
                invalid = True
            elif not missing and not MANDATORY_FIELDS[field](pp[field]):
                invalid = True

        is_valid = not missing and (not validate or not invalid)
        # print("{valid}: {passport}".format(valid=is_valid, passport=pp))
        if is_valid:
            number_of_passports += 1
        else:
            number_of_invalid_passports += 1

    return (number_of_passports, number_of_invalid_passports)


(valid, invalid) = passport_scanner(False)
print("part1: valid: {0} invalid: {1}".format(valid, invalid))

(valid, invalid) = passport_scanner(True)
print("part2: valid: {0} invalid: {1}".format(valid, invalid))