def search_quadruplets(arr, target):
    arr.sort()
    quadruplets = []
    for i in range(len(arr) - 3):
        for j in range(i + 1, len(arr) - 2):
            left = j + 1
            right = len(arr) - 1
            while left < right:
                tmp_sum = arr[i] + arr[j] + arr[left] + arr[right]
                if tmp_sum == target:
                    quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                elif tmp_sum > target:
                    right -= 1  
                else:
                    left += 1
    return quadruplets


def main():
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()
