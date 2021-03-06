def find_first_missing_positive(nums):
    i, n = 0, len(nums)
    while i < len(nums):
        if nums[i] > 0:
            j = nums[i] - 1
            if j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        else:
            i += 1
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return -1


def main():
    print(find_first_missing_positive([-3, 1, 5, 4, 2]))
    print(find_first_missing_positive([3, -2, 0, 1, 2]))
    print(find_first_missing_positive([3, 2, 5, 1]))


main()
