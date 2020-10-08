from collections import deque


def find_permutations(nums):
    result = []
    queue = deque()
    queue.append([])

    for num in nums:
        n = len(queue)
        for _ in range(n):
            tmp = queue.popleft()
            for i in range(len(tmp) + 1):
                new_tmp = list(tmp)
                new_tmp.insert(i, num)
                if len(new_tmp) == len(nums):
                    result.append(new_tmp)
                else:
                    queue.append(new_tmp)

    return result


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
