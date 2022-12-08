def main(path):
    print("part 1:")
    tmp = part1(path)
    print("part 2:")
    part2(tmp)

def combine_path(paths:[]):
    return '/'.join(paths)
def part1(path):
    f = open(path, "r")
    tree_path = []
    memory = {'/':0}
    for line in f:
        line = line.split()
        if line[0] =='$':
            if line[1] == 'cd':
                if line[2] != '..':
                    tree_path.append(line[2])
                else:
                    tree_path.pop(-1)
        elif line[0] == 'dir':
            memory[combine_path(tree_path+[line[1]])] = 0
        else:
            for i in range(len(tree_path)):
                memory[combine_path(tree_path[:i+1])] += int(line[0])
    print(memory)
    res = 0
    for val in memory:
        if memory[val] <= 100000:
            res += memory[val]
    print(res)
    return [*memory.values()]



def part2(memory):
    used = memory.pop(0)
    full = 70000000
    required = 30000000
    available = full - used
    memory.sort()
    for el in memory:
        if el + available > required:
            print(el)
            return
