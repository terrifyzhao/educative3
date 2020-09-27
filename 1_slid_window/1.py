def max_sub_array_of_size_k(k, arr):
    n = len(arr)
    start, end = 0, len(arr) - 1

    sum = 0
    max_sum = -100
    for i in range(n):
        sum += arr[i]
        if i >= k:
            sum -= arr[start]
            start += 1
        max_sum = max(max_sum, sum)

    return max_sum


def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
