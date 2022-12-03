def calc_priority(data):
    res = 0
    for el in data:
        if el.isupper():
            res += 27 + ord(el) - ord('A')
        else:
            res += 1 + ord(el) - ord('a')
    return res


def part1(path):
    f = open(path, "r")
    to_reorganise = []
    for line in f:
        line = line.strip('\n')
        mid = int(len(line) / 2)
        left = sorted(line[:mid])
        right = sorted(line[mid:])
        id_left = 0
        id_right = 0
        tmp_to_reorganise = []
        while id_left < mid and id_right < mid:
            if left[id_left] == right[id_right]:
                tmp_to_reorganise.append(left[id_left])
                id_left += 1
                id_right += 1
            elif left[id_left] < right[id_right]:
                id_left += 1
            else:
                id_right += 1

        to_reorganise += list(set(tmp_to_reorganise))
    res = calc_priority(to_reorganise)
    print(res)


def part2(path):
    f = open(path, "r")
    to_reorganise = []
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        a = set(lines[i].strip('\n'))
        b = set(lines[i + 1].strip('\n'))
        c = set(lines[i + 2].strip('\n'))
        to_reorganise += (list(*a.intersection(b, c)))
    res = calc_priority(to_reorganise)
    print(res)


def main(path):
    print("Part 1:")
    part1(path)
    print("Part 2:")
    part2(path)
