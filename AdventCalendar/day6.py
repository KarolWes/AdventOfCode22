def main(path):
    print("part 1:")
    part1(path)
    print("part 2:")
    part2(path)


def part1(path):
    f = open(path, "r")
    code = f.readline()
    i = 4
    while i < len(code):
        if len(set(code[i-4:i])) == 4:
            print(i)
            return
        else:
            i+=1


def part2(path):
    f = open(path, "r")
    code = f.readline()
    i = 14
    while i < len(code):
        if len(set(code[i - 14:i])) == 14:
            print(i)
            return
        else:
            i += 1
