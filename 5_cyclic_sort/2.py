def find_missing_number(nums):
    i = 0
    while i < len(nums):
        index = nums[i]
        if index < len(nums) and nums[index] != nums[i]:
            nums[i], nums[index] = nums[index], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return 0


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()
