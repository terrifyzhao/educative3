from heapq import *


def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    min_heap = []

    for i, c in enumerate(capital):
        heappush(min_heap, [c, i])

    while numberOfProjects:
        numberOfProjects -= 1
        while min_heap and initialCapital >= min_heap[0][0]:
            c, index = heappop(min_heap)
        initialCapital += profits[index]
    return initialCapital


def main():
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
