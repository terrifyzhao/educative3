from collections import deque


def can_construct(originalSeq, sequences):
    sortedOrder = []
    if len(originalSeq) <= 0:
        return False

    # a. Initialize the graph
    inDegree = {}  # count of incoming edges
    graph = {}  # adjacency list graph
    for sequence in sequences:
        for num in sequence:
            inDegree[num] = 0
            graph[num] = []

    # b. Build the graph
    for seq in sequences:
        for i in range(1, len(seq)):
            p, c = seq[i - 1], seq[i]
            inDegree[c] += 1
            graph[p].append(c)

    if len(inDegree) != len(originalSeq):
        return False

    # c. Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    while sources:
        if len(sources) > 1:
            return False

        if originalSeq[len(sortedOrder)] != sources[0]:
            return False

        node = sources.popleft()
        sortedOrder.append(node)
        for n in graph[node]:
            inDegree[n] -= 1
            if inDegree[n] == 0:
                sources.append(n)

    # if sortedOrder's size is not equal to original sequence's size, there is no unique way to construct
    return len(sortedOrder) == len(originalSeq)


def main():
    print("Can construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
    print("Can construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
    print("Can construct: " +
          str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()
