blocks = [
    [
        (0, 0), (0, 1), (0, 2), (0, 3),1
    ],
    [
        (0, 1), (1, 0), (1, 1), (1, 2), (2, 1),3
    ],
    [
        (0, 0), (0, 1), (0, 2), (1, 2), (2, 2),3
    ],
    [
        (0, 0), (1, 0), (2, 0), (3, 0),4
    ],
    [
        (0, 0), (0, 1), (1, 0), (1, 1),2
    ]
]


def main(path):
    # print("part 1:")
    # part1(path)
    print("part 2:")
    part2(path)


def part1(path):
    f = open(path, "r")
    jet = f.readline()
    size = len(jet)
    round = 0
    block_id = 0
    jet_id = 0
    x_size = 7
    max_y = 0
    occupated = []
    while round < 1000000000000:
        block = blocks[block_id]
        y = max_y + 3
        x = 2
        can_fall = True
        while can_fall:
            dir = 1 if jet[jet_id % size] == '>' else -1
            new_x = x + dir
            possible = True
            for el in block[-2::-1]:
                if not(0 <= el[1] + new_x < x_size) or (el[0] + y, el[1] + new_x) in occupated:
                    possible = False
                    break
            if possible:
                x = new_x
            for el in block[-2::-1]:
                if not(0 <= el[0] + y - 1) or (el[0] + y - 1, el[1] + x) in occupated:
                    can_fall = False
                    break
            if can_fall:
                y -= 1
            else:
                for el in block[-2::-1]:
                    if max_y < el[0]+y+1:
                        max_y = el[0]+y+1
                    occupated.append((el[0] + y, el[1] + x))
            jet_id+=1
        block_id = (block_id + 1)%5
        print(round)
        round+=1
    print(max_y)


def part2(path):
    f = open(path, "r")
    jet = f.readline()
    size = len(jet)
    round = 0
    block_id = 0
    jet_id = 0
    x_size = 7
    max_y = 0
    occupated = {0:[]}
    while round < 1000000000000:
        block = blocks[block_id]
        y = max_y + 3
        for i in range(max_y+1, y+block[-1]):
            occupated[i]=[]
        x = 2
        can_fall = True
        while can_fall:
            dir = 1 if jet[jet_id % size] == '>' else -1
            new_x = x + dir
            possible = True
            for el in block[-2::-1]:
                if not (0 <= el[1] + new_x < x_size) or el[1] + new_x in occupated[el[0] + y]:
                    possible = False
                    break
            if possible:
                x = new_x
            for el in block[-2::-1]:
                if not (0 <= el[0] + y - 1) or el[1] + x in occupated[el[0] + y - 1]:
                    can_fall = False
                    break
            if can_fall:
                y -= 1
            else:
                for el in block[-2::-1]:
                    if max_y < el[0] + y + 1:
                        max_y = el[0] + y + 1
                    occupated[el[0] + y].append(el[1] + x)
            jet_id += 1
        block_id = (block_id + 1) % 5
        print(round)
        round += 1
    print(max_y)