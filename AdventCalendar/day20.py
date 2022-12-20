def main(path):
    print("Part 1:")
    part1(path)
    print("Part 2:")
    part2(path)


def part1(path):
    f = open(path, "r")
    order = list(map(int, f.readlines()))
    size = len(order)
    ordinal = [*range(0, size)]
    nums = {}
    for i in range(size):
        nums[i] = order[i]
    for el in range(size):
        id = ordinal.index(el)
        ordinal.pop(id)
        new_pos = (id + nums[el]) %(size-1)
        ordinal.insert(new_pos, el)
    for k, val in nums.items():
        if val == 0:
            zero_id = ordinal.index(k)
    print(zero_id)
    el1 = ordinal[(zero_id + 1000) % size]
    el2 = ordinal[(zero_id + 2000) % size]
    el3 = ordinal[(zero_id + 3000) % size]
    print((el1, el2, el3))
    print((nums[el1], nums[el2], nums[el3]))
    print(nums[el1] + nums[el2] + nums[el3])


def part2(path):
    f = open(path, "r")
    decryption_key = 811589153
    order = list(map(int, f.readlines()))
    order = [x*decryption_key for x in order]
    size = len(order)
    ordinal = [*range(0, size)]
    nums = {}
    for i in range(size):
        nums[i] = order[i]

    for round in range(10):
        print(round)
        for el in range(size):
            id = ordinal.index(el)
            ordinal.pop(id)
            new_pos = (id + nums[el]) % (size - 1)
            ordinal.insert(new_pos, el)

    for k, val in nums.items():
        if val == 0:
            zero_id = ordinal.index(k)
    print(zero_id)
    el1 = ordinal[(zero_id + 1000) % size]
    el2 = ordinal[(zero_id + 2000) % size]
    el3 = ordinal[(zero_id + 3000) % size]
    print((el1, el2, el3))
    print((nums[el1], nums[el2], nums[el3]))
    print(nums[el1] + nums[el2] + nums[el3])


