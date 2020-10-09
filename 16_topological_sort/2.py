def is_scheduling_possible(tasks, prerequisites):
    graph = {i: [] for i in range(tasks)}
    in_degree = {i: 0 for i in range(tasks)}

    for p, c in prerequisites:
        graph[p].append(c)
        in_degree[c] += 1

    from collections import deque
    queue = deque()
    for k, v in in_degree.items():
        if v == 0:
            queue.append(k)
    res = []
    while queue:
        node = queue.popleft()
        res.append(node)
        for n in graph[node]:
            in_degree[n] -= 1
            if in_degree[n] == 0:
                queue.append(n)

    if len(res) != tasks:
        return False

    return True


def main():
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))


main()
