from heapq import *


def rearrange_string(str):
    dic = {}
    for num in str:
        dic[num] = dic.get(num, 0) + 1

    max_heap = []
    for k, v in dic.items():
        heappush(max_heap, [-v, k])

    res = []
    pre_char, pre_count = None, 0
    while max_heap:
        count, char = heappop(max_heap)

        if pre_char and -pre_count > 0:
            heappush(max_heap, [pre_count, pre_char])

        res.append(char)
        pre_char = char
        pre_count = count + 1

    if len(res) == len(str):
        return ''.join(res)

    return ""


def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))


main()
