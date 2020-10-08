from heapq import *


def find_maximum_distinct_elements(nums, k):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
    res = 0
    min_heap = []
    for num, frequency in dic.items():
        if frequency == 1:
            res += 1
        else:
            heappush(min_heap, [frequency, num])

    while min_heap and k > 0:
        frequency, num = heappop(min_heap)

        k = k - frequency + 1
        if k >= 0:
            res += 1

    if k > 0:
        res -= k

    return res


def main():
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
