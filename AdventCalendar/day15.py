def main(path):
    print("part 1:")
    part1(path)
    print("part 2:")
    part2(path)


lines = {}

def prepare_dict(num_lines):
    global lines
    for i in range(0, num_lines+1):
        lines[i] = []

def dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def coverage(start, dist):
    res = []
    for i in range(dist):
        up_y = start[1] - dist + i
        down_y = start[1] + dist - i
        for j in range(start[0] - i, start[0] + i+1):
            res.append((j, up_y))
            res.append((j, down_y))
    return res

def coverage_theory(start, dist, goal):
    if start[1] - dist <= goal <= start[1] + dist:
        i = dist - abs(start[1] - goal)
        return [start[0]-i, start[0]+i]


def coverage_theory_wout_goal(start, dist, lim):
    global lines
    for i in range(dist):
        up_y = start[1] - dist + i
        down_y = start[1] + dist - i
        if 0 <= up_y <= lim:
            lines[up_y] += [[start[0]-i, start[0]+i]]
        if 0 <= down_y <= lim:
            lines[down_y] += [[start[0] - i, start[0] + i]]
    lines[start[1]] += [[start[0] - dist, start[0] + dist]]


def count_on_level(coverage, level):
    return len([x for x in coverage if x[1] == level])


def find_overlap(coords):
    res = []
    current = coords[0]
    for i in range(1, len(coords)):
        new = coords[i]
        if new[0] <= current[1]:
            if new[1] > current[1]:
                current[1] = new[1]
        else:
            if new[0] - current[1] == 1:
                current[1] = new[1]
            else:
                res.append(current)
                current = new
    res.append(current)
    return res

def part1(path):
    f = open(path, "r")
    cov = []
    beacons = []
    goal = 10
    for line in f:
        line = line.split()
        s_x = int(line[2][2:len(line[2])-1])
        s_y = int(line[3][2:len(line[3])-1])
        b_x = int(line[8][2:len(line[8])-1])
        b_y = int(line[9][2:len(line[9])])

        if b_y == goal:
            beacons.append(b_x)

        d = dist((s_x, s_y), (b_x, b_y))

        tmp = coverage_theory((s_x, s_y), d, goal)
        if tmp is not None:
            cov.append(tmp)
    cov = sorted(cov, key=lambda x:x[0])
    print(cov)
    overlap = find_overlap(cov)
    print(overlap)
    beacons = set(beacons)
    res = 0
    for el in overlap:
        res += el[1]-el[0] +1
        for b in beacons:
            if el[0] <= b <= el[1]:
                res -= 1
    print(res)



def part2(path):
    global lines

    f = open(path, "r")
    goal = 4_000_000
    prepare_dict(goal)

    for line in f:
        line = line.split()
        s_x = int(line[2][2:len(line[2]) - 1])
        s_y = int(line[3][2:len(line[3]) - 1])
        b_x = int(line[8][2:len(line[8]) - 1])
        b_y = int(line[9][2:len(line[9])])

        d = dist((s_x, s_y), (b_x, b_y))
        print(d)
        coverage_theory_wout_goal((s_x, s_y), d, goal)
    # print(lines)
    x = 0
    y = 0
    for k in lines:
        reducted = find_overlap(sorted(lines[k], key=lambda x:x[0]))
        if len(reducted) > 1:
            y = k
            x = reducted[0][1]+1
            break
    print(x*4_000_000 + y)