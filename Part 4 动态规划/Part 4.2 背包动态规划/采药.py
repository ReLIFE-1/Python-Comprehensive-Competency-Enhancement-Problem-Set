# 读取输入
T, M = map(int, input().split())
herbs = []
for _ in range(M):
    herbs.append(list(map(int, input().split())))

# 初始化DP数组
dp = [0] * (T + 1)

# 动态规划处理
for item in herbs:
    t, v = item[0], item[1]
    for j in range(T, t - 1, -1):
        if dp[j - t] + v > dp[j]:
            dp[j] = dp[j - t] + v

# 输出结果
print(dp[T])