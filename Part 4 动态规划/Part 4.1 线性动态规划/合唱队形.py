n = int(input())
h = list(map(int, input().split()))

# f1[i] 表示以 h[i] 结尾的最长上升子序列的长度
f1 = [1] * n
# f2[i] 表示以 h[i] 开头的最长下降子序列的长度
f2 = [1] * n

# 从左向右计算最长上升子序列
for i in range(n):
    for j in range(i):
        if h[i] > h[j]:
            f1[i] = max(f1[i], f1[j] + 1)

# 从右向左计算最长上升子序列 (等价于从左向右的最长下降子序列)
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if h[i] > h[j]:
            f2[i] = max(f2[i], f2[j] + 1)

# 合并计算以每个点为顶点的合唱队形的最大长度
max_k = 0
for i in range(n):
    # h[i] 被计算了两次，所以要减 1
    k = f1[i] + f2[i] - 1
    if k > max_k:
        max_k = k

# 总人数减去最长合唱队形的人数，即为需要出列的人数
print(n - max_k)