import math


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    diff = 10000

    for i in range(len(arr)):
        num = arr[i]
        left = i + 1
        right = len(arr) - 1
        while left < right:
            tmp_sum = num + arr[left] + arr[right]
            if tmp_sum == target_sum:
                return 0

            if abs(target_sum - tmp_sum) < diff:
                diff = abs(target_sum - tmp_sum)

            if tmp_sum > target_sum:
                right -= 1
            else:
                left += 1

    return target_sum-diff

def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()
