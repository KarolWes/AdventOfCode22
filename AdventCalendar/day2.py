def main(path):
    f = open(path, "r")
    print("Part 1:")
    part1(path)
    print("Part 2:")
    part2(path)


def part1(f):
    points = 0
    for line in f:
        line = line.split()
        elf = ord(line[0])-ord('A')
        you = ord(line[1])-ord('X')
        points += you + 1
        if elf == you:
            points += 3
        elif you == (elf + 1)%3:
            points += 6
    print(points)


def part2(f):
    points = 0
    for line in f:
        line = line.split()
        elf = ord(line[0]) - ord('A')
        you = ord(line[1]) - ord('X')
        if you == 0:
            points += (elf + 2) % 3 + 1
        elif you == 1:
            points += elf + 1 + 3
        else:
            points += (elf + 1) % 3 + 1 + 6
    print(points)
