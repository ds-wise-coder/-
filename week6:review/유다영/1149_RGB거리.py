n = int(input())
dp = []

for i in range(n):
    dp.append(list(map(int, input().split())))

# print(dp)

for i in range(1, len(dp)):
    # red
    dp[i][0] = dp[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    # green
    dp[i][1] = dp[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    # blue
    dp[i][2] = dp[i][2] + min(dp[i - 1][0], dp[i - 1][1])

# 최솟값 출력
print(min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))
