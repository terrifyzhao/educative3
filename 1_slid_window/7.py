def length_of_longest_substring(arr, k):
    start = 0
    max_len = 0

    count_0 = 0
    for i in range(len(arr)):
        num = arr[i]
        if num == 0:
            count_0 += 1

        while count_0 > k:
            num = arr[start]
            if num == 0:
                count_0 -= 1
            start += 1
        max_len = max(max_len, i - start + 1)
    return max_len


def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring(
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
