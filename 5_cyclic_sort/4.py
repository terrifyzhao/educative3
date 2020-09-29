def find_duplicate(nums):
    i = 0
    # res = []
    while i < len(nums):
        index = nums[i] - 1
        if nums[index] != nums[i]:
            nums[i], nums[index] = nums[index], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return nums[i]

    return -1


def main():
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))


main()
