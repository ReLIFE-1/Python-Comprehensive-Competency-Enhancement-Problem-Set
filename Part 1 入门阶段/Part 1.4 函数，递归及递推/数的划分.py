n, k = map(int, input().split())

# 初始化DP表
dp = [[0]*(n+1) for _ in range(k+1)]
dp[0][0] = 1  # 分成0部分和为0的方法

# 填充DP表
for i in range(1, k+1):  # 份数
    for j in range(1, n+1):  # 总和
        if j >= i:
            dp[i][j] = dp[i-1][j-1] + dp[i][j-i]
        else:
            dp[i][j] = 0

print(dp[k][n])