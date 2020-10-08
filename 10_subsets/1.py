def find_subsets(nums):
    subsets = []

    subsets.append([])
    for num in nums:
        n = len(subsets)
        for i in range(n):
            tmp = list(subsets[i])
            tmp.append(num)
            subsets.append(tmp)

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
