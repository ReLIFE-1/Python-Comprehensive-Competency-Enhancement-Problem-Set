n, m = map(int, input().split())

items = []
for _ in range(m):
    v, p = map(int, input().split())
    items.append((v, p))

dp = [0] * (n + 1)

for v, p in items:
    for i in range(n, v - 1, -1):
        dp[i] = max(dp[i], dp[i - v] + v * p)

print(dp[n])