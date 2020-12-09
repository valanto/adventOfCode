import os
import re


def get_instructions():
    instructions = []
    file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
    for line in file:
        match = re.match(r"^([a-z]{3})\s+([+-]?\d+)$", line)
        command = match.group(1).strip()
        val = int(match.group(2).strip())
        instructions.append(dict(command=command, value=val, ran=0))
    file.close()
    return instructions


def run_program(instructions, index, acc):
    if index > len(instructions):
        print("reached end")
        return acc
    instruction = instructions[index]
    command = instruction["command"]
    val = instruction["value"]
    ran = instruction["ran"]

    if ran == 1:
        return acc

    instructions[index]["ran"] += 1

    if command == "nop":
        index += 1

    if command == "acc":
        acc += val
        index += 1

    if command == "jmp":
        index += val

    return run_program(instructions, index, acc)


def get_acc_before_crash(instructions, acc=0):
    return run_program(instructions, 0, acc)


def run_program_and_fix(instructions, index, acc, check_fix):
    if index >= len(instructions) - 1:
        print("reached end: {0}:{1}".format(index, len(instructions)))
        return acc

    instruction = instructions[index]
    command = instruction["command"]
    if index == check_fix:
        if command == "jmp":
            command = "nop"
        elif command == "nop":
            command = "jmp"
    val = instruction["value"]
    ran = instruction["ran"]

    if ran == 1:
        return False

    instructions[index]["ran"] += 1

    if command == "nop":
        index += 1

    if command == "acc":
        acc += val
        index += 1

    if command == "jmp":
        index += val

    return run_program_and_fix(instructions, index, acc, check_fix)


def get_acc_with_fix(instructions, acc=0):
    index = 0
    for instruction in instructions:
        if instruction["command"] == "nop" or instruction["command"] == "jmp":
            acc = run_program_and_fix(get_instructions(), 0, acc, index)
            if acc is not False:
                break
        index += 1

    return acc


print("part1: {0}".format(get_acc_before_crash(get_instructions())))
print("part2: {0}".format(get_acc_with_fix(get_instructions())))
