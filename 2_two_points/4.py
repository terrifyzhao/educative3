def search_triplets(arr):
    arr.sort()

    res = []

    for i in range(len(arr)):
        left = i + 1
        right = len(arr) - 1
        num = -arr[i]
        while left < right:
            if arr[left] + arr[right] == num:
                res.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            elif arr[left] + arr[right] < num:
                left += 1
            else:
                right -= 1
    return res


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


main()
