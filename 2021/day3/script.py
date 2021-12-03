import os

def find_common_bit(lines, pos):
    zero = []
    one = []
    for line in lines:
        bit = line[pos]
        if bit == '0':
            zero.append(line)
        if bit == '1':
            one.append(line)

    return (zero, one) 

def get_ox(lines, i):
    if len(lines) == 1:
        return lines[0]

    if i == 12:
        return lines[0]

    (zero, one) = find_common_bit(lines, i)

    if len(one) - len(zero) >=0:
        return get_ox(one, i + 1)
    else:
        return get_ox(zero, i + 1)

def get_co(lines, i):
    if len(lines) == 1:
        return lines[0]

    if i == 12:
        return lines[0]

    (zero, one) = find_common_bit(lines, i)

    if len(zero) - len(one) <= 0:
        return get_co(zero, i + 1)
    else:
        return get_co(one, i + 1)


def part2():
    file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
    lines = []
    for line in file:
        lines.append(line.strip())

    ox = get_ox(lines, 0)
    co = get_co(lines, 0)
    return int(ox, 2) * int(co,2)

    


def part1():
    zero = [0,0,0,0,0,0,0,0,0,0,0,0]
    one = [0,0,0,0,0,0,0,0,0,0,0,0]
    file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
    for line in file:
        i = 0
        for bit in line.strip():
            if bit == '0':
                zero[i]= zero[i]+1
            if bit == '1':
                one[i] = one[i]+1
            i = i + 1
    gamma_string = ""
    epsilon_string = ""
    for j in range(12):
        if zero[j] > one[j]:
            gamma_string = gamma_string + '0'
            epsilon_string = epsilon_string + '1'            
        else:
            gamma_string = gamma_string + '1'
            epsilon_string = epsilon_string + '0'            
    return int(gamma_string, 2) * int(epsilon_string, 2)

print("part1: {0}".format(part1()))
print("part2: {0}".format(part2()))
