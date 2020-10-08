def find_range(arr, key):
    result = [- 1, -1]

    start, end = 0, len(arr) - 1
    index = -1
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            index = mid
            break
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    start, end = index, index
    if index == -1:
        return [-1, -1]
    while start > 0 and arr[start] == arr[start - 1]:
        start -= 1

    while end < len(arr) - 1 and arr[end] == arr[end + 1]:
        end += 1

    return [start, end]


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
