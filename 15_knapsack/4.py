def can_partition(num):
    s = sum(num)
    n = len(num)
    dp = [[False for _ in range(int(s / 2) + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = True

    for i in range(int(s / 2) + 1):
        dp[0][i] = i == num[0]

    for i in range(n):
        for j in range(int(s / 2) + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i - 1][j - num[i]]

    num1 = 0
    for i in range(s // 2, -1, -1):
        if dp[-1][i]:
            num1 = i
            break
    num2 = s-num1
    return abs(num1-num2)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
