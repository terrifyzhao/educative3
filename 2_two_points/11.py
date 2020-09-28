import math


def shortest_window_sort(arr):
    left = 0
    right = len(arr) - 1

    while left < len(arr) - 1 and arr[left] <= arr[left + 1]:
        left += 1
    if left == len(arr) - 1:
        return 0
    while right > 1 and arr[right] >= arr[right - 1]:
        right -= 1

    min_num = min(arr[left:right + 1])
    max_num = max(arr[left:right + 1])

    while left > 0 and arr[left - 1] > min_num:
        left -= 1
    while right < len(arr) - 1 and arr[right + 1] < max_num:
        right += 1
    return right - left + 1


def main():
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))


main()
