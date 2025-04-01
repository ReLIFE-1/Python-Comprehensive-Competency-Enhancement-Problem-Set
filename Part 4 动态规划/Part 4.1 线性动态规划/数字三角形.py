n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
dp = [[0]*(i+1) for i in range(n+1)]
dp[0][0] = a[0][0]
for i in range(1,n):
    for j in range(0,i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + a[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + a[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + a[i][j]

print(max(dp[-2]))
