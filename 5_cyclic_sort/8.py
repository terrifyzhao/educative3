def find_first_k_missing_positive(nums, k):
    n = len(nums)
    i = 0
    missingNumbers = []
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] > 0 and j < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1 and len(missingNumbers) < k:
            missingNumbers.append(i + 1)

    while len(missingNumbers) < k:
        missingNumbers.append(max(nums) + 1)
        nums.append(max(nums) + 1)

    return missingNumbers


def main():
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))


main()
