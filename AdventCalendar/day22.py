directions = {0:[0,1], 1:[1,0], 2:[0,-1], 3:[-1,0]}
def parser(path):
    f = open(path, "r")
    tmp = []
    max_len = 0
    for line in f:
        if line == '\n':
            instruction = f.readline()
            break
        line = line.rstrip()
        tmp.append(line)
        max_len = max(max_len, len(line))

    max_len += 2
    mapa = [' ' * max_len]
    for line in tmp:
        mapa.append(' ' + line + ' '*(max_len-(len(line)+1)))
    mapa.append(' ' * max_len)
    new_ins = []
    tmp = 0
    for i in instruction:
        try:
            i = int(i)
            tmp *= 10
            tmp += i
        except:
            new_ins.append(tmp)
            new_ins.append(i)
            tmp = 0
    if tmp > 0:
        new_ins.append(tmp)
    instruction = new_ins
    print(instruction)
    return mapa, instruction

def part1(path):
    mapa, instruction = parser(path)
    row = 1
    for i, el in enumerate(mapa[1]):
        if el == '.':
            col = i
            break
    print((row, col))
    dir = 0
    pos = [row,col]
    for i in instruction:
        if type(i) == int:
            steps = i

            new_pos = [pos[0]+directions[dir][0], pos[1]+directions[dir][1]]
            while steps > 0 and mapa[new_pos[0]][new_pos[1]] != '#':
                if mapa[new_pos[0]][new_pos[1]] == ' ':
                    safeguard = pos[:]
                    new_pos = [pos[0] - directions[dir][0], pos[1] - directions[dir][1]]
                    while mapa[new_pos[0]][new_pos[1]] != ' ':
                        new_pos = [new_pos[0] - directions[dir][0], new_pos[1] - directions[dir][1]]
                    new_pos = [new_pos[0] + directions[dir][0], new_pos[1] + directions[dir][1]]
                    if mapa[new_pos[0]][new_pos[1]] == '#':
                        pos = safeguard
                        break
                steps -= 1
                pos = new_pos[:]
                new_pos = [pos[0] + directions[dir][0], pos[1] + directions[dir][1]]
        else:
            if i == 'R':
                dir = (dir + 1) % 4
            else:
                dir = (dir - 1) % 4


    ans = 1000*pos[0] + 4*pos[1] + dir
    print(ans)





def part2(path):
    f = open(path, "r")
    print("Way too complicated")


def main(path):
    print("Part 1:")
    part1(path)
    print("Part 2:")
    part2(path)
