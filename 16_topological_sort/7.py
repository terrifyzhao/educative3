from collections import deque


def find_trees(nodes, edges):
    if nodes <= 0:
        return []

    # with only one node, since its in-degrees will be 0, therefore, we need to handle it separately
    if nodes == 1:
        return [0]

    # a. Initialize the graph
    inDegree = {i: 0 for i in range(nodes)}  # count of incoming edges
    graph = {i: [] for i in range(nodes)}  # adjacency list graph

    for parent, child in edges:
        inDegree[child] += 1
        inDegree[parent] += 1
        graph[parent].append(child)
        graph[child].append(parent)

    queue = deque()
    for k, v in inDegree.items():
        if v == 1:
            queue.append(k)
    length = nodes
    while length > 2:
        leaves_size = len(queue)
        length -= leaves_size
        for i in range(leaves_size):
            node = queue.popleft()
            for n in graph[node]:
                inDegree[n] -= 1
                if inDegree[n] == 1:
                    queue.append(n)

    return list(queue)


def main():
    print("Roots of MHTs: " +
          str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
    print("Roots of MHTs: " +
          str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
    print("Roots of MHTs: " +
          str(find_trees(4, [[1, 2], [1, 3]])))


main()
