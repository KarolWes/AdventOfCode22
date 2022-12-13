from collections import deque as queue

# Direction vectors
dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]


def main(path):
    print("part 1:")
    part1(path)
    print("part 2:")
    part2(path)


def isValid(vis, row, col):
    # If cell lies out of bounds
    if row < 0 or col < 0 or row > 40 or col > 112:
        return False

    # If cell is already visited
    if vis[row][col]:
        return False

    # Otherwise
    return True


def isValid2(cur_val, new_val):
    if new_val - cur_val > 1:
        return False
    return True

def isValid3(cur_val, new_val):
    if cur_val - new_val > 1:
        return False
    return True


# Function to perform the BFS traversal
def BFS(grid, vis, start, stop):
    q = queue()
    q.append((start, 0))
    vis[start[0]][start[1]] = True
    while len(q) > 0:
        cell, val = q.popleft()
        if cell == stop:
            print()
            print(val)
            return
        x = cell[0]
        y = cell[1]
        print(grid[x][y], end=" ")

        # q.pop()

        # Go to the adjacent cells
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if isValid(vis, adjx, adjy) and isValid2(grid[x][y], grid[adjx][adjy]):
                q.append(((adjx, adjy), val + 1))
                vis[adjx][adjy] = True


def BFSnew(grid, vis, start, stop_val):
    q = queue()
    q.append((start, 0))
    vis[start[0]][start[1]] = True
    while len(q) > 0:
        cell, val = q.popleft()
        x = cell[0]
        y = cell[1]
        if grid[x][y] == stop_val:
            print()
            print(val)
            return
        print(grid[x][y], end=" ")

        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if isValid(vis, adjx, adjy) and isValid3(grid[x][y], grid[adjx][adjy]):
                q.append(((adjx, adjy), val + 1))
                vis[adjx][adjy] = True


def part1(path):
    f = open(path, "r")
    mapa = []
    data = f.readlines()
    visited = []

    for i in range(len(data)):
        line = data[i].strip()
        row = len(line)
        tmp = []
        for j in range(len(line)):
            if line[j] == 'S':
                start = (i, j)
                tmp.append(0)
            elif line[j] == 'E':
                stop = (i, j)
                tmp.append(25)
            else:
                tmp.append(ord(line[j]) - ord('a'))
        mapa.append(tmp)
        visited.append([False] * row)
    BFS(mapa, visited, start, stop)


def part2(path):
    f = open(path, "r")
    mapa = []
    data = f.readlines()
    visited = []

    for i in range(len(data)):
        line = data[i].strip()
        row = len(line)
        tmp = []
        for j in range(len(line)):
            if line[j] == 'S':
                start = (i, j)
                tmp.append(0)
            elif line[j] == 'E':
                stop = (i, j)
                tmp.append(25)
            else:
                tmp.append(ord(line[j]) - ord('a'))
        mapa.append(tmp)
        visited.append([False] * row)
    BFSnew(mapa, visited, stop, 0)
