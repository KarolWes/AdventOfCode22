# based on solution by NORMIE101
INF = int(1e12)

def main(path):
    print("part 1:")
    part1(path)
    print("part 2:")
    part2(path)


def FW(nodes, mapa):
    dist = {v: {u: INF for u in nodes} for v in nodes}

    for v in nodes:
        dist[v][v] = 0
        for u in mapa[v][1]:
            dist[v][u] = 1

    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def part1(path):
    f = open(path, "r")
    mapa = {}
    nodes = []
    start = 'AA'
    from_node = 'AA'
    time_limit = 30
    release = 0
    for line in f:
        line = line.split()
        mapa[line[1]] = [int(line[4].split('=')[1].strip(';')), [*map(lambda x: x.strip(','), line[9:])]]
        nodes.append(line[1])
    dist = FW(nodes, mapa)
    non_zero = [v for v in nodes if mapa[v][0] > 0]

    def generate_open_options(pos, open_valves, time_left):
        for next in non_zero_valves:
            if next not in open_valves and distances[pos][next] <= time_left:
                open_valves.append(next)
                yield from generate_open_options(
                    next, open_valves, time_left - distances[pos][next] - 1
                )
                open_valves.pop()

        yield copy(open_valves)

    def get_order_score(open_order, time_left):
        now, ans = "AA", 0
        for pos in open_order:
            time_left -= distances[now][pos] + 1
            ans += valves[pos].flow_rate * time_left
            now = pos
        return ans

    def solution_1():
        return max(get_order_score(o, 30) for o in generate_open_options("AA", [], 30))



    print(release)






def part2(path):
    f = open(path, "r")
