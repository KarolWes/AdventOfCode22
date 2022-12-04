def part1(path):
    f = open(path, "r")
    res = 0
    for line in f:
        line = line.split(',')
        first = list(map(int,line[0].split("-")))
        second = list(map(int,line[1].split("-")))
        first = {*range(first[0], first[1] + 1)}
        second = {*range(second[0], second[1] + 1)}
        inter = first.intersection(second)
        if first == inter or second == inter:
            res +=1
    print(res)


def part2(path):
    f = open(path, "r")
    res = 0
    for line in f:
        line = line.split(',')
        first = list(map(int, line[0].split("-")))
        second = list(map(int, line[1].split("-")))
        first = {*range(first[0], first[1] + 1)}
        second = {*range(second[0], second[1] + 1)}
        inter = first.intersection(second)
        if len(inter) != 0:
            res +=1
    print(res)



def main(path):
    print("Part 1:")
    part1(path)
    print("Part 2:")
    part2(path)
