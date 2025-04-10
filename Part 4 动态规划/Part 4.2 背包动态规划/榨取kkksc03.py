n,M,T = map(int,input().split())
items = []
for _ in range(n):
    items.append(list(map(int,input().split())))

def max_wishes(items):
    dp = [[0]*(T + 1) for _ in range(M+1)]
    for item in items:
        m,t = item[0],item[1]
        for i in range(M, m - 1, -1): #采取倒序遍历,0-1背包
            for j in range(T, t - 1, -1):
                dp[i][j] = max(dp[i-m][j-t] + 1,dp[i][j])
    return dp[M][T]

print(max_wishes(items))
    

