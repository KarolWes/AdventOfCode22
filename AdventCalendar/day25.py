def main(path):
    print("part 1:")
    part1(path)
    print("part 2:")
    part2()


def part1(path):
    f = open(path, "r")
    nump = []
    for line in f:
        line = list(line.strip())
        tmp = []
        for el in line:
            if el == '=':
                tmp.append(-2)
            elif el == '-':
                tmp.append(-1)
            else:
                tmp.append(int(el))
        n = 0
        for el in tmp:
            n *= 5
            n += el
        nump.append(n)
    val = sum(nump)
    ans = []
    while val > 0:
        div = val // 5
        mod = val % 5
        if mod > 2:
            mod -= 5
            div += 1
        ans.insert(0, mod)
        val = div
    print(ans)
    for i in range(len(ans)):
        if ans[i] == -1:
            ans[i] = '-'
        elif ans[i] == -2:
            ans[i] = '='
        else:
            ans[i] = str(ans[i])
    print(''.join(ans))


def part2():
    print("Advent ended")
    print("40/49 stars collected")
    print("Merry Christmas")
    print("Coded by KarolWes, Dec. 2022")
