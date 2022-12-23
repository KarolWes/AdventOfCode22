def main(path):
    print("part 1:")
    part1(path)
    print("part 2:")
    part2(path)


direction_full = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
directions = [[(-1, -1), (-1, 0), (-1, 1)],
              [(1, -1), (1, 0), (1, 1)],
              [(-1, -1), (0, -1), (1, -1)],
              [(-1, 1), (0, 1), (1, 1)]]


def part1(path):
    more = 11
    f = open(path, "r")
    mapa = []
    poses = []
    line = f.readline()
    line = '.' * more + line.strip() + '.' * more
    size = len(line)
    for i in range(more):
        mapa.append(['.'] * size)
    mapa.append(list(line))
    for line in f:
        line = list('.' * more + line.strip() + '.' * more)
        mapa.append(line)
    for i in range(more):
        mapa.append(['.'] * size)
    for line in mapa:
        print(line)
    size_x = len(mapa[0])
    size_y = len(mapa)
    round = 10
    for i in range(size_y):
        for j in range(size_x):
            if mapa[i][j] == '#':
                poses.append((i, j))
    for _ in range(round):
        new_poses = []
        duplicates = []
        seen = set()
        for pos in poses:
            res = True
            for check in direction_full:
                res &= mapa[pos[0] + check[0]][pos[1] + check[1]] == '.'
            if res:
                new_poses.append([pos,pos])
            else:
                for dir in directions:
                    res = True
                    for check in dir:
                        res &= mapa[pos[0] + check[0]][pos[1] + check[1]] == '.'
                    if res:
                        np = (pos[0] + dir[1][0], pos[1] + dir[1][1])
                        if np in seen:
                            duplicates.append(np)
                        else:
                            seen.add(np)
                        new_poses.append([pos, np])
                        break
        tmp = []
        for old, new in new_poses:

            if new not in duplicates:
                mapa[old[0]][old[1]] = '.'
                mapa[new[0]][new[1]] = '#'
                tmp.append(new)
            else:
                tmp.append(old)
        poses = tmp[:]
        directions.append(directions.pop(0))
        print("___")
        for line in mapa:
            print(line)
    max_x = 0
    max_y = 0
    min_x = 10000000
    min_y = 10000000
    for el in poses:
        max_x = max(max_x, el[1])
        max_y = max(max_y, el[0])
        min_x = max(min_x, el[1])
        min_y = max(min_y, el[0])
    count = 0
    for i in range(min_y, max_y+1):
        for j in range(min_x, max_x+1):
            if mapa[i][j] == '.':
                count+=1
    print(count)




def part2(path):
    f = open(path, "r")
