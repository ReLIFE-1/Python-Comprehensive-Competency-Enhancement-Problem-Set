n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
prefix = [[0] * (m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + a[i-1][j-1]

max_length = 0
for k in range(1, min(n, m)+1):
    # 遍历所有可能的右下方坐标
    for i in range(k, n+1):
        for j in range(k, m+1):
            # 计算子正方形的和
            total = prefix[i][j] - prefix[i-k][j] - prefix[i][j-k] + prefix[i-k][j-k]
            # 如果是全1则更新max_length
            if total == k * k:
                max_length = max(max_length, k)

print(max_length)
