from heapq import *


def find_Kth_smallest(lists, k):
    heap_min = []

    for list in lists:
        heappush(heap_min, (list[0], 0, list))

    while heap_min and k > 1:
        num, index, list = heappop(heap_min)

        index += 1
        if index < len(list):
            heappush(heap_min, (list[index], index, list))
        k -= 1

    return heap_min[0][0]


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[5, 8, 9], [1, 7]], 3)))


main()
