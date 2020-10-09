from collections import deque


def topological_sort(vertices, edges):
    sortedOrder = []

    graph = {i: [] for i in range(vertices)}
    in_degree = {i: 0 for i in range(vertices)}

    for parent, child in edges:
        in_degree[child] += 1
        graph[parent].append(child)

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

    if len(sortedOrder) != vertices:
        return []

    return sortedOrder


def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
