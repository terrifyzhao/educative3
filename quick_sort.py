def quick_sort(arr):
    start, end = 0, len(arr) - 1
    sort(arr, start, end)


def sort(arr, start, end):
    left, right = start, end
    if left < right:
        pivot = arr[left]
        while left != right:
            while left < right and arr[right] > pivot:
                right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] < pivot:
                left += 1
            arr[right] = arr[left]
        arr[left] = pivot
        sort(arr, start, left - 1)
        sort(arr, right + 1, end)


if __name__ == '__main__':
    nums = [23, 4, 1, 523, 2, 3, 111]
    quick_sort(nums)
    print(nums)
