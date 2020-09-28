def make_squares(arr):
    n = len(arr)
    res = [0 for _ in range(n)]

    left, right = 0, n - 1
    i = n - 1
    while left <= right and i >= 0:
        l = arr[left] * arr[left]
        r = arr[right] * arr[right]
        if l > r:
            res[i] = l
            left += 1
        else:
            res[i] = r
            right -= 1
        i -= 1
    return res


def main():
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
