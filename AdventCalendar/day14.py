def main(path):
    print("part 1:")
    part1(path)
    print("part 2:")
    part2(path)

def simulate(mapa, lim, x_min):
    act_x = 500
    act_y = 0
    can_move = True
    while can_move:
        if act_y >= lim:
            return True
        if mapa[act_y+1][act_x-x_min-1] == '.':
            can_move = True
            act_y = act_y + 1
        elif mapa[act_y+1][act_x-1-x_min-1] == '.':
            can_move = True
            act_x = act_x -1
            act_y = act_y + 1
        elif mapa[act_y+1][act_x+1-x_min-1] == '.':
            can_move = True
            act_x = act_x +1
            act_y = act_y + 1
        else:
            can_move = False
    mapa[act_y][act_x-x_min-1] = 'o'
    return False


def simulate2(mapa, x_min):
    act_x = 500
    act_y = 0
    can_move = True
    while can_move:
        if mapa[act_y+1][act_x-x_min-1] == '.':
            can_move = True
            act_y = act_y + 1
        elif mapa[act_y+1][act_x-1-x_min-1] == '.':
            can_move = True
            act_x = act_x -1
            act_y = act_y + 1
        elif mapa[act_y+1][act_x+1-x_min-1] == '.':
            can_move = True
            act_x = act_x +1
            act_y = act_y + 1
        else:
            can_move = False
    if act_y == 0:
        return True
    mapa[act_y][act_x-x_min-1] = 'o'
    return False
def part1(path):
    f = open(path, "r")
    min_x = 1000
    min_y = 1000
    max_x = 0
    max_y = 0
    coords = []
    for line in f:
        tmp =[]
        line = line.split('->')
        for el in line:
            val = [*map(int, el.strip().split(','))]
            min_x = min(min_x, val[0])
            min_y = min(min_y, val[1])
            max_x = max(max_x, val[0])
            max_y = max(max_y, val[1])
            tmp.append(val)
        coords.append(tmp)
    min_y = 0
    min_x -=2
    x_size = max_x - min_x
    y_size = max_y+2

    mapa = []
    for i in range(y_size):
        mapa.append(['.']*x_size)

    for line in coords:
        for i in range(len(line) -1):
            if line[i][0] == line[i+1][0]:
                l = min(line[i][1], line[i+1][1])
                r = max(line[i][1], line[i+1][1])
                for j in range(l, r+1):
                    mapa[j-min_y-1][line[i][0]-min_x-1] = '#'
            else:
                l = min(line[i][0], line[i+1][0])
                r = max(line[i][0], line[i+1][0])
                for j in range(l,r+1):
                    mapa[line[i][1]-min_y-1][j-min_x-1] = '#'
    mapa[0][500 - min_x - 1] = '+'
    for line in mapa:
        for el in line:
            print(el, end = '')
        print()

    gen = 0
    while not simulate(mapa, max_y, min_x):
        gen+=1
    print(gen)




def part2(path):
    f = open(path, "r")
    min_x = 1000
    min_y = 1000
    max_x = 0
    max_y = 0
    coords = []
    for line in f:
        tmp = []
        line = line.split('->')
        for el in line:
            val = [*map(int, el.strip().split(','))]
            min_x = min(min_x, val[0])
            min_y = min(min_y, val[1])
            max_x = max(max_x, val[0])
            max_y = max(max_y, val[1])
            tmp.append(val)
        coords.append(tmp)
    min_y = 0

    y_size = max_y + 3
    x_size = y_size*2+1
    min_x = 500-(x_size+1)//2

    mapa = []
    for i in range(y_size):
        mapa.append(['.'] * x_size)

    for line in coords:
        for i in range(len(line) - 1):
            if line[i][0] == line[i + 1][0]:
                l = min(line[i][1], line[i + 1][1])
                r = max(line[i][1], line[i + 1][1])
                for j in range(l, r + 1):
                    mapa[j - min_y][line[i][0] - min_x - 1] = '#'
            else:
                l = min(line[i][0], line[i + 1][0])
                r = max(line[i][0], line[i + 1][0])
                for j in range(l, r + 1):
                    mapa[line[i][1] - min_y][j - min_x - 1] = '#'
    mapa[0][500 - min_x - 1] = '+'
    mapa[-1] = ['#'] * x_size
    for line in mapa:
        for el in line:
            print(el, end='')
        print()

    gen = 1
    while not simulate2(mapa, min_x):
        gen += 1
    print(gen)


