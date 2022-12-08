import numpy as np
def main(path):
    print("part 1:")
    part1(path)
    print("part 2:")
    part2(path)


def part1(path):
    f = open(path, "r")
    grid = []
    for line in f:
        grid.append([*map(int, line.strip())])
    rows = len(grid)
    cols = len(grid[0])
    grid = np.array(grid)
    visibility = np.array([[True]*cols]*rows)

    for i in range(1,rows-1):
        for j in range(1,cols-1):
            up = max(grid[:i, j])
            down = max(grid[i+1:, j])
            left = max(grid[i, :j])
            right = max(grid[i, j+1:])
            central = grid[i,j]

            dirs = [up, down, left, right]
            visibility[i,j] = any(central > dirs)
    print(visibility.sum())



def part2(path):
    f = open(path, "r")
    grid = []
    for line in f:
        grid.append([*map(int, line.strip())])
    rows = len(grid)
    cols = len(grid[0])
    grid = np.array(grid)

    res = 0
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            up = grid[:i, j]
            down = grid[i + 1:, j]
            left = grid[i, :j]
            right = grid[i, j + 1:]
            central = grid[i, j]
            dirs = [reversed(up), down, reversed(left), right]

            scenic = 1
            for dir in dirs:
                tmp = 0
                for el in dir:
                    if el < central:
                        tmp+=1
                    else:
                        tmp+=1
                        break
                scenic*=tmp
            res = max(res, scenic)
    print(res)
