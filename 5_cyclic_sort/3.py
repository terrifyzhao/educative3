def find_missing_numbers(nums):
    missingNumbers = []
    i = 0

    while i < len(nums):
        index = nums[i] - 1
        if index < len(nums) and nums[index] != nums[i]:
            nums[i], nums[index] = nums[index], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if i + 1 != nums[i]:
            missingNumbers.append(i + 1)

    return missingNumbers


def main():
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers([2, 4, 1, 2]))
    print(find_missing_numbers([2, 3, 2, 1]))


main()
