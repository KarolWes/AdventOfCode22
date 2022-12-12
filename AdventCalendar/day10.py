def main(path):
    print("part 1:")
    part1(path)
    print("part 2:")
    part2(path)


def part1(path):
    f = open(path, "r")
    X = 1
    cycle = 1
    res = []
    for line in f:
        line = line.strip().split()
        cycle += 1
        if cycle%20 == 0:
            print(str(cycle) + ": " + str(X))
            res.append(X*cycle)
        if line[0] != "noop":
            cycle += 1
            X += int(line[1])
            if cycle % 20 == 0:
                print(str(cycle) + ": " + str(X))
                res.append(X * cycle)
    ans = sum(res[::2])
    print(ans)


def part2(path):
    f = open(path, "r")
    X = 1
    pos = [X-1, X, X+1]
    screen = []
    for i in range(6):
        screen.append(['.']*40)

    cycle = 1
    for line in f:
        line = line.strip().split()
        if cycle%40 in pos:
            screen[cycle//40][cycle%40] = '#'

        if line[0] != "noop":
            cycle += 1
            X += int(line[1])
            pos = [X - 1, X, X + 1]
            if cycle%40 in pos:
                screen[cycle//40][cycle%40] = '#'
        cycle += 1
    for line in screen:
        for el in line:
            if el == '.':
                print(' ', end='')
            else:
                print(el, end='')
        print()


