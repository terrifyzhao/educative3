def count_subsets(num, sum):
    n = len(num)
    dp = [[-1 for x in range(sum + 1)] for y in range(n)]

    for i in range(n):
        dp[i][0] = 1

    for i in range(1, sum + 1):
        dp[0][i] = 1 if i == num[0] else 0

    for i in range(1, n):
        for j in range(1, sum + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= num[i]:
                dp[i][j] += dp[i - 1][j - num[i]]
    return dp[-1][-1]


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
