import operator

ops = {'+': operator.add, '*': operator.mul, '^': operator.pow}


def main(path):
    print("part 1:")
    part1(path)
    print("part 2:")
    part2(path)


def parser(entry):
    res = []
    res.append(list(map(int, entry[1].split(':')[1].split(', '))))
    tmp = entry[2].split('=')[1].strip().split()
    if tmp[2] == 'old':
        res.append('^')
        res.append(2)
    else:
        res.append(tmp[1])
        res.append(int(tmp[2]))
    res.append(int(entry[3].split('by')[1].strip()))
    tmp = []
    tmp.append(int(entry[4].split('monkey')[1].strip()))
    tmp.append(int(entry[5].split('monkey')[1].strip()))
    res.append(tmp)
    res.append(0)
    return res


def part1(path):
    f = open(path, "r")
    test = f.readlines()
    data = []

    for i in range(0, len(test), 7):
        data.append(parser(test[i:i + 7]))

    for round in range(20):
        for obj in data:
            mul = False
            add = False
            squ = False

            if obj[1] == '*':
                mul = True
            if obj[1] == '+':
                add = True
            if obj[1] == '^':
                squ = True
            new_vals = []
            for val in obj[0]:
                obj[-1] += 1
                if add:
                    new_vals.append((val + obj[2]) // 3)
                if mul:
                    new_vals.append((val * obj[2]) // 3)
                if squ:
                    new_vals.append((val ** 2) // 3)
            obj[0] = []
            for val in new_vals:
                if val % obj[3] == 0:
                    data[obj[4][0]][0].append(val)
                else:
                    data[obj[4][1]][0].append(val)
    ans = []
    for el in data:
        ans.append(el[-1])
    ans.sort()
    print(ans[-1] * ans[-2])


def part2(path):
    f = open(path, "r")
    test = f.readlines()
    data = []

    for i in range(0, len(test), 7):
        data.append(parser(test[i:i + 7]))

    lim = 1
    for obj in data:
        lim *= obj[3]

    for round in range(10000):

        for obj in data:
            for val in obj[0]:
                obj[-1] += 1
                tmp = ops[obj[1]](val, obj[2])
                if tmp > lim:
                    tmp = tmp % lim
                if tmp % obj[3] == 0:
                    data[obj[4][0]][0].append(tmp)
                else:
                    data[obj[4][1]][0].append(tmp)
            obj[0] = []

    ans = []
    for el in data:
        ans.append(el[-1])
    ans.sort()
    print(ans[-1] * ans[-2])
