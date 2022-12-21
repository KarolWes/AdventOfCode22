def part1(path):
    f = open(path, "r")
    costs = {'ore':0, 'clay':0, 'obsidian':0, 'geode':0}
    income = {'ore':1, 'clay':0, 'obsidian':0, 'geode':0}
    storage = {'ore':0, 'clay':0, 'obsidian':0, 'geode':0}
    maxs = {'ore':0, 'clay':0, 'obsidian':0, 'geode':0}
    for line in f:
        stack = []
        line = line.split()
        costs['ore'] = {'ore': int(line[6])}
        costs['clay'] = {'ore': int(line[12])}
        costs['obsidian'] = {'ore': int(line[18]), 'clay':int(line[21])}
        costs['geode'] = {'ore': int(line[27]), 'obsidian':int(line[30])}
        time = 0
        stack.append([time, income, storage, []])
        while len(stack) != 0:
            current = stack.pop(0)
            if current[0] < 24:
                # wait
                new_income = current[1].copy()
                if len(current[3]) > 0:
                    new_income[current[3][0]]+=1
                    current[3].pop(0)
                stack.append([current[0] + 1, new_income,
                              {x: current[2][x] + current[1][x] for x in income.keys()}, current[3]])

                for key, val in costs.items():
                    res = True
                    for k, v in val.items():
                        if current[2][k] < v:
                            res = False
                    if res:
                        new_storage = {x: current[2][x] + current[1][x] for x in income.keys()}
                        for k, v in val.items():
                            new_storage[k] -= v
                        stack.append([current[0] + 1, new_income,
                                      new_storage, current[3] + [key]])

            else:
                maxs = {i: max(maxs[i], current[2][i]) for i in income.keys()}
        print(maxs)








def part2(path):
    f = open(path, "r")




def main(path):
    print("Part 1:")
    part1(path)
    print("Part 2:")
    part2(path)
