def main(path):
    part2(path)


def part1(path):
    f = open(path, "r")
    data = f.read().split("\n")
    maks = 0
    tmp = 0
    for val in data:
        if val != "":
            tmp += int(val)
        else:
            maks = max(maks, tmp)
            tmp = 0
    maks = max(maks, tmp)
    print(maks)


def part2(path):
    f = open(path, "r")
    data = f.read().split("\n")
    sums = []
    tmp = 0
    for val in data:
        if val != "":
            tmp += int(val)
        else:
            sums.append(tmp)
            tmp = 0
    sums.sort(reverse=True)
    print(sum(sums[:3]))
