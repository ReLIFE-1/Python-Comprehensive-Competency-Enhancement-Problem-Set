l = int(input())

# 步骤 1: 预计算 1 到 l 每个数的约数个数
# d[i] 存储整数 i 的约数个数
d = [0] * (l + 1)
for i in range(1, l + 1):
    # i 是其所有倍数的一个约数
    for j in range(i, l + 1, i):
        d[j] += 1

# 步骤 2: 预计算约数个数的前缀和
# s[i] 存储 d[1] + d[2] + ... + d[i]
s = [0] * (l + 1)
for i in range(1, l + 1):
    s[i] = s[i-1] + d[i]

# 步骤 3: 计算最终答案
# 遍历所有可能的 p1 (1 <= p1 < l)
# 对于每个 p1, p2 的范围是 1 <= p2 <= l - p1
# 满足条件的组合数是 d[p1] * (d[1] + ... + d[l-p1])
ans = 0
for p1 in range(1, l):
    ans += d[p1] * s[l - p1]

print(ans)