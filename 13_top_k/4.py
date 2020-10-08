from heapq import *


def minimum_cost_to_connect_ropes(ropeLengths):
    min_heap = []
    for rope in ropeLengths:
        heappush(min_heap, rope)

    rope, res = 0, 0
    while len(min_heap) > 1:
        rope = heappop(min_heap) + heappop(min_heap)
        res += rope
        heappush(min_heap, rope)

    return res


def main():
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
