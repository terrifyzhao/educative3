from heapq import *


def find_k_frequent_numbers(nums, count):
    topNumbers = []
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1

    max_heap = []
    for k, v in dic.items():
        heappush(max_heap, [-v, k])

    for i in range(count):
        topNumbers.append(heappop(max_heap)[1])
    
    return topNumbers


def main():
    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
