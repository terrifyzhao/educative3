from collections import deque


def find_subarrays(arr, target):
    product = 1
    start = 0
    res = []
    for i in range(len(arr)):
        product *= arr[i]
        while product >= target and start < len(arr):
            product /= arr[start]
            start += 1

        tmp_list = deque()
        for j in range(i, start-1, -1):
            tmp_list.appendleft(arr[j])
            res.append(list(tmp_list))

    return res


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))


main()
