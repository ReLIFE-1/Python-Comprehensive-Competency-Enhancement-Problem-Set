def knapsack(N, V, items):
    dp = [0] * (V + 1)
    for i in range(N):
        v, w = items[i]
        for j in range(V, v - 1, -1): #倒序遍历
            dp[j] = max(dp[j], dp[j - v] + w)

    return dp[V]

N, V = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
print(knapsack(N, V, items))
