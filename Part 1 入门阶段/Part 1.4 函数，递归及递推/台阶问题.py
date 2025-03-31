N, K = map(int, input().split())

# 初始化dp数组
dp = [0] * (N + 1)
dp[0] = 1
mod = 100003

# 初始化窗口和
window_sum = dp[0]

# 计算dp[i]
for i in range(1, N + 1):
    dp[i] = window_sum % mod
    window_sum = (window_sum + dp[i]) % mod
    if i >= K:
        window_sum = (window_sum - dp[i - K]) % mod

print(dp[N])