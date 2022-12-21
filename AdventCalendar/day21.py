import operator

ops = {'+': operator.add, '*': operator.mul, '-': operator.sub, '/': operator.floordiv, '=':operator.eq}
complementary = {'-': operator.add, '/': operator.mul, '+': operator.sub, '*': operator.floordiv, '=':operator.eq}
def main(path):
    print("Part 1:")
    # part1(path)
    print("Part 2:")
    part2(path)


def part1(path):
    f = open(path, "r")
    monkeys = {}
    monkey_numps = {}
    for line in f:
        line = line.strip().split(': ')
        try:
            nump = int(line[1])
            monkey_numps[line[0]] = nump
        except:
            monkeys[line[0]] = line[1].split()
    print(monkey_numps)
    while 'root' not in monkey_numps.keys():
        for key, val in monkeys.items():
            if key not in monkey_numps.keys():
                if type(val[0]) != int and val[0] in monkey_numps.keys():
                    val[0] = monkey_numps[val[0]]
                if type(val[2]) != int and val[2] in monkey_numps.keys():
                    val[2] = monkey_numps[val[2]]
                if type(val[0]) == int and type(val[2]) == int:
                    monkey_numps[key] = ops[val[1]](val[0], val[2])
                monkeys[key] = val
    print(monkey_numps['root'])



def part2(path):
    f = open(path, "r")
    monkeys = {}
    monkey_numps = {}
    for line in f:
        line = line.strip().split(': ')
        try:
            nump = int(line[1])
            monkey_numps[line[0]] = nump
        except:
            monkeys[line[0]] = line[1].split()
    print(monkey_numps)
    while type(monkeys['root'][0]) != int and type(monkeys['root'][2])!= int:
        for key, val in monkeys.items():
            if key not in monkey_numps.keys():
                if type(val[0]) != int and val[0] in monkey_numps.keys():
                    val[0] = monkey_numps[val[0]]
                if type(val[2]) != int and val[2] in monkey_numps.keys():
                    val[2] = monkey_numps[val[2]]
                if type(val[0]) == int and type(val[2]) == int:
                    monkey_numps[key] = ops[val[1]](val[0], val[2])
                monkeys[key] = val
    print(monkeys['root'])
    current = monkeys['root'][0] if type(monkeys['root'][0]) != int else monkeys['root'][2]
    curr_val = monkeys['root'][2] if type(monkeys['root'][0]) != int else monkeys['root'][0]
    monkey_numps[current] = curr_val
    while 'humn' not in monkey_numps.keys():
        if type(monkeys[current][0]) != int:
            new_key = monkeys[current][0]
            new_val = monkeys[current][2]
            curr_val = complementary[monkeys[current][1]](curr_val, new_val)
        else:
            new_key = monkeys[current][2]
            new_val = monkeys[current][0]
            if monkeys[current][1] == '+':
                curr_val = curr_val - new_val
            if monkeys[current][1] == '-':
                curr_val = new_val-curr_val
            if monkeys[current][1] == '/':
                curr_val = new_val//curr_val
            if monkeys[current][1] == '*':
                curr_val = curr_val//new_val
        monkey_numps[new_key] = curr_val
        current = new_key
    print(monkey_numps['humn'])




