def find_single_number(arr):

    res = 0
    for a in arr:
        res ^= a

    return res


def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))


main()
