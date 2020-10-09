def find_target_subsets(num, s):
    totalSum = sum(num)
    n = len(num)

    if (s + totalSum) % 2 != 0:
        return 0

    aim_sum = (s + totalSum) // 2

    dp = [[-1 for x in range(aim_sum + 1)] for y in range(n)]

    for i in range(n):
        dp[i][0] = 1

    for i in range(1, aim_sum + 1):
        dp[0][i] = 1 if i == num[0] else 0

    for i in range(1, n):
        for j in range(1, aim_sum + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= num[i]:
                dp[i][j] += dp[i - 1][j - num[i]]
    return dp[-1][-1]


def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()
