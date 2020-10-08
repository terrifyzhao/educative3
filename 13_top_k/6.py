from heapq import *


def sort_character_by_frequency(str):
    dic = {}
    for num in str:
        dic[num] = dic.get(num, 0) + 1

    max_heap = []
    for k, v in dic.items():
        heappush(max_heap, [-v, k])

    res = ''
    while max_heap:
        v, k = heappop(max_heap)
        res += k*(-v)

    return res


def main():
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
