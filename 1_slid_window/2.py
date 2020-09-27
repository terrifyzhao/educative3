import math


def smallest_subarray_with_given_sum(s, arr):
    n = len(arr)
    start = 0
    min_len = 10000
    arr_sum = 0

    for i in range(n):
        arr_sum += arr[i]
        while arr_sum >= s:
            arr_sum -= arr[start]
            min_len = min(min_len, i - start + 1)
            start += 1
    return min_len


def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
