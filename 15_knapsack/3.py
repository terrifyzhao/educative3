def can_partition(num, sum):
    n = len(num)
    dp = [[False for _ in range(sum + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = True

    for s in range(1, sum + 1):
        dp[0][s] = num[0] == s

    for i in range(1, n):
        for j in range(sum, -1, -1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i - 1][j - num[i]]

    return dp[-1][-1]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
