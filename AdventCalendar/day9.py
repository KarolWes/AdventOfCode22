import math


def main(path):
    print("part 1:")
    part1(path)
    print("part 2:")
    part2(path)

def dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2
def part1(path):
    f = open(path, "r")
    dir_dict = {'U':[-1,0], 'D':[1,0], 'L':[0,-1], 'R':[0,1]}
    head = [0,0]
    tail = [0,0]
    poses = [str(tail)]
    for line in f:
        line = line.split()
        dir = line[0]
        steps = int(line[1])
        for i in range(steps):
            head[0]+=dir_dict[dir][0]
            head[1]+=dir_dict[dir][1]
            d = dist(head, tail)
            if d == 4:
                tail[0] += dir_dict[dir][0]
                tail[1] += dir_dict[dir][1]
            elif d == 5:
                tail[0] += dir_dict[dir][0]
                tail[1] += dir_dict[dir][1]
                if dir == 'U' or dir == 'D':
                    if tail[1] > head[1]:
                        tail[1] -=1
                    else:
                        tail[1] += 1
                else:
                    if tail[0] > head[0]:
                        tail[0] -=1
                    else:
                        tail[0] += 1
            poses.append(str(tail))
    print(len(set(poses)))



def part2(path):
    f = open(path, "r")
    dir_dict = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
    tails = []
    for i in range(10):
        tails.append([0,0])
    poses = [str(tails[-1])]
    for line in f:
        line = line.split()
        dir = line[0]
        steps = int(line[1])
        for i in range(steps):
            tails[0][0] += dir_dict[dir][0]
            tails[0][1] += dir_dict[dir][1]
            for i in range(1, len(tails)):
                d = dist(tails[i-1], tails[i])
                if tails[i][1] > tails[i-1][1]:
                    new_dir = 'L'
                elif tails[i][1] < tails[i-1][1]:
                    new_dir = 'R'
                if tails[i][0] > tails[i-1][0]:
                    new_dir = 'U'
                elif tails[i][0] < tails[i-1][0]:
                    new_dir = 'D'
                if d == 4:
                    tails[i][0] += dir_dict[new_dir][0]
                    tails[i][1] += dir_dict[new_dir][1]
                elif d > 4:
                    tails[i][0] += dir_dict[new_dir][0]
                    tails[i][1] += dir_dict[new_dir][1]
                    if new_dir == 'U' or new_dir == 'D':
                        if tails[i][1] > tails[i-1][1]:
                            tails[i][1] -= 1
                        else:
                            tails[i][1] += 1
                    else:
                        if tails[i][0] > tails[i-1][0]:
                            tails[i][0] -= 1
                        else:
                            tails[i][0] += 1
            poses.append(str(tails[-1]))
    print(len(set(poses)))
