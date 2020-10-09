def find_order(tasks, prerequisites):
    sortedOrder = []

    graph = {i: [] for i in range(tasks)}
    in_degree = {i: 0 for i in range(tasks)}

    for parent, child in prerequisites:
        in_degree[child] += 1
        graph[parent].append(child)
    from collections import deque
    queue = deque()
    for k, v in in_degree.items():
        if v == 0:
            queue.append(k)

    while queue:
        node = queue.popleft()
        sortedOrder.append(node)
        for n in graph[node]:
            in_degree[n] -= 1
            if in_degree[n] == 0:
                queue.append(n)

    if len(sortedOrder) != tasks:
        return []

    return sortedOrder


def main():
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()
