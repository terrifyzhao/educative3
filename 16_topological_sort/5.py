from collections import deque


def find_order(words):
    if len(words) == 0:
        return ""

    sortedOrder = []

    graph = {}
    in_degree = {}
    for word in words:
        for c in word:
            graph[c] = []
            in_degree[c] = 0

    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        for j in range(min(len(word1), len(word2))):
            w1 = word1[j]
            w2 = word2[j]
            if w1 != w2:
                graph[w1].append(w2)
                in_degree[w2] += 1
                break

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

    if len(sortedOrder) != len(in_degree):
        return ''

    return ''.join(sortedOrder)


def main():
    print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
    print("Character order: " + find_order(["cab", "aaa", "aab"]))
    print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()
