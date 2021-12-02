import os

def part1():
    h=0
    v=0
    file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
    for line in file:
        (move, increment) = line.strip().split(' ')
        if(move == 'forward'):
            h = h + int(increment)
        if(move == 'up'):
            v = v - int(increment)
        if(move == 'down'):
            v = v + int(increment)
       
    return h * v

def part2():
    h=0
    v=0
    a=0
    file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
    for line in file:
        (move, increment) = line.strip().split(' ')
        if(move == 'forward'):
            h = h + int(increment)
            v = v + (a * int(increment))
        if(move == 'up'):
            a = a - int(increment)
        if(move == 'down'):
            a = a + int(increment)
       
    return h * v


print("part1: {0}".format(part1()))
print("part2: {0}".format(part2()))
