grid = []


def surrounded(start, size):
    visited = [[[False for k in range(size)] for j in range(size)] for i in range(size)]
    dir = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
    global grid
    queue = []
    queue.append(start)
    visited[start[0]][start[1]][start[1]] = True

    while queue:
        s = queue.pop(-1)
        if s == [0,0,0]:
            return False
        for d in dir:
            new_s = [s[0]+d[0], s[1]+d[1], s[2]+d[2]]
            if 0 <= new_s[0] < size and 0 <= new_s[1] < size and 0 <= new_s[2] < size:
                if not visited[new_s[0]][new_s[1]][new_s[2]]:
                    if not grid[new_s[0]][new_s[1]][new_s[2]]:
                        queue.append(new_s)
                        visited[new_s[0]][new_s[1]][new_s[2]] = True
    return True

def main(path):
    print("part 1:")
    part1(path)
    print("part 2:")
    part2(path)


def part1(path):
    f = open(path, "r")
    global grid
    size = 25
    res = 0
    grid = [[[False for k in range(size)] for j in range(size)] for i in range(size)]
    for line in f:
        line = list(map(int, line.split(',')))
        grid[line[0]+1][line[1]+1][line[2]+1] = True

    for i in range(1, size-1):
        for j in range(1, size-1):
            for m in range(1, size-1):
                if grid[i][j][m]:
                    if not grid[i - 1][j][m]:
                        res += 1
                    if not grid[i + 1][j][m]:
                        res += 1
                    if not grid[i][j - 1][m]:
                        res += 1
                    if not grid[i][j + 1][m]:
                        res += 1
                    if not grid[i][j][m - 1]:
                        res += 1
                    if not grid[i][j][m + 1]:
                        res += 1

    print(res)


def part2(path):
    f = open(path, "r")
    global grid
    size = 25
    res = 0
    grid = [[[False for k in range(size)] for j in range(size)] for i in range(size)]
    for line in f:
        line = list(map(int, line.split(',')))
        grid[line[0] + 1][line[1] + 1][line[2] + 1] = True

    for i in range(1, size - 1):
        for j in range(1, size - 1):
            for m in range(1, size - 1):
                if not grid[i][j][m]:
                    print([i, j, m])
                    if surrounded([i, j, m], size):
                        grid[i][j][m] = True

    for i in range(1, size - 1):
        for j in range(1, size - 1):
            for m in range(1, size - 1):
                if grid[i][j][m]:
                    if not grid[i - 1][j][m]:
                        res += 1
                    if not grid[i + 1][j][m]:
                        res += 1
                    if not grid[i][j - 1][m]:
                        res += 1
                    if not grid[i][j + 1][m]:
                        res += 1
                    if not grid[i][j][m - 1]:
                        res += 1
                    if not grid[i][j][m + 1]:
                        res += 1

    print(res)
