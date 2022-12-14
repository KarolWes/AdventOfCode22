from AdventCalendar import day13datafile as datafile
res = 0

def main():
    print("part 1:")
    part1()
    print("part 2:")
    part2()

def compare_ints(left, right, val):
    global res
    if left != right:
        if left < right:
            print(val)
            res += val
        return True
    else:
        return False

def compare_lists(left, right, val):
    global res
    left_len = len(left)
    right_len = len(right)
    for m in range(min(left_len, right_len)):
        if type(left[m]) == type(right[m]):
            if type(left[m]) == int:
                if compare_ints(left[m], right[m], val):
                    return True
            else:
                if compare_lists(left[m], right[m], val):
                    return True
        else:
            if type(left[m]) == int:
                left[m] = [left[m]]
            else:
                right[m] = [right[m]]
            if compare_lists(left[m], right[m], val):
                return True
    if left_len < right_len:
        res += val
        print(val)
        return True
    else:
        return False


def part1():
    data = datafile.main

    for i in range(0, len(data), 2):
        left = data[i]
        right = data[i + 1]
        val = i//2 + 1
        compare_lists(left, right, val)
    global res
    print(res)





def part2():
    pass
