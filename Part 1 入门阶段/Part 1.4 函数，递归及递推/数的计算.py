def count_arr(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = 1
        for j in range(1,i // 2 + 1):
            dp[i] += dp[j]
    
    return dp[n]

n = int(input())
print(count_arr(n))
