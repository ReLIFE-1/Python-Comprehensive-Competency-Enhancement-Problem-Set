def knapsack(N,V,items):
    dp = [0] * (V + 1)
    for i in range(1,N+1):
        v,w = items[i-1]
        for j in range(1,V+1): # 正序遍历
            if j >= v:
                dp[j] = max(dp[j],dp[j - v] + w)
    return dp[V]  
        
N, V = map(int, input().split())
items = [list(map(int,input().split())) for _ in range(N)]
print(knapsack(N, V, items))