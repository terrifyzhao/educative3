def search_min_diff_element(arr, key):
    start, end = 0, len(arr) - 1

    if key > arr[-1]:
        return arr[-1]
    if key < arr[0]:
        return arr[0]

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    return arr[end] if abs(arr[start] - key) > abs(arr[end] - key) else arr[start]


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


main()
