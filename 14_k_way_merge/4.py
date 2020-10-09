from heapq import *
import math


def find_smallest_range(lists):
    min_heap = []
    start, end = 0, 10000

    max_num = -1000

    for list in lists:
        heappush(min_heap, (list[0], 0, list))
        max_num = max(max_num, list[0])

    while len(min_heap) == len(lists):
        num, index, list = heappop(min_heap)

        if end - start > max_num - num:
            end = max_num
            start = num

        index += 1
        if len(list) > index:
            heappush(min_heap, (list[index], index, list))
            max_num = max(max_num, list[index])

    return [start, end]


def main():
    print("Smallest range is: " +
          str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()
