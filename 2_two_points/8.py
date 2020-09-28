def dutch_flag_sort(arr):
    left = 0
    right = len(arr) - 1
    i = 0
    while i <= right:

        num = arr[i]
        if num == 0:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        elif num == 1:
            i += 1
        else:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1


def main():
    arr = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr)
    print(arr)


main()
