def main(path):
    print("part 1:")
    part1(path)
    print("part 2:")
    part2(path)


def part1(path):
    f = open(path, "r")
    lines = f.readlines()
    line = lines[0]
    stack = []
    instructions = []
    i = 0
    while line != "\n":
        stack.append(line.rstrip('\n'))
        i+=1
        line = lines[i]
    i+=1
    while i < len(lines):
        line = lines[i]
        line = line.rstrip('\n')
        line = line.split()
        instructions.append([int(line[1]), int(line[3]), int(line[5])])
        i+=1
    nums = [*(map(int, stack[-1].split()))]
    ran = nums[-1] - nums[0] + 1
    new_stack = [[]]*ran
    for line in stack[:-1]:
        line = line.replace("    ", " [] ")
        line = line.split()
        i = 0
        for el in line:
            if el != '[]':
                new_stack[i] = [el[1]] + new_stack[i]
            i+=1
    print(new_stack)
    for line in instructions:
        source = line[1]
        dest = line[2]
        for _ in range(line[0]):
            new_stack[dest-1].append(new_stack[source-1].pop(-1))
    for line in new_stack:
        print(line[-1], end="")
    print("\n")






def part2(path):
    f = open(path, "r")
    lines = f.readlines()
    line = lines[0]
    stack = []
    instructions = []
    i = 0
    while line != "\n":
        stack.append(line.rstrip('\n'))
        i += 1
        line = lines[i]
    i += 1
    while i < len(lines):
        line = lines[i]
        line = line.rstrip('\n')
        line = line.split()
        instructions.append([int(line[1]), int(line[3]), int(line[5])])
        i += 1
    nums = [*(map(int, stack[-1].split()))]
    ran = nums[-1] - nums[0] + 1
    new_stack = [[]] * ran
    for line in stack[:-1]:
        line = line.replace("    ", " [] ")
        line = line.split()
        i = 0
        for el in line:
            if el != '[]':
                new_stack[i] = [el[1]] + new_stack[i]
            i += 1
    print(new_stack)
    for line in instructions:
        source = line[1]
        dest = line[2]
        tmp = new_stack[source - 1][-1:-1-line[0]:-1]
        new_stack[dest - 1] += tmp[-1::-1]
        del new_stack[source - 1][-1:-1 - line[0]:-1]
    for line in new_stack:
        print(line[-1], end="")
    print("\n")
