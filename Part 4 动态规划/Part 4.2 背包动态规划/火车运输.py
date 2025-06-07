# 题目: P10987 [蓝桥杯 2023 国 Python A] 火车运输
# 核心思想: 二维背包动态规划

n, a, b = map(int, input().split())
w = list(map(int, input().split()))

# 初始化dp表，dp[i][j]表示车厢1重i，车厢2重j是否可行
dp = [[False for _ in range(b + 1)] for _ in range(a + 1)]
dp[0][0] = True # 初始状态，两个车厢都为空

# 遍历每个物品
for weight in w:
    # 从后往前遍历，防止重复使用同一个物品
    for i in range(a, -1, -1):
        for j in range(b, -1, -1):
            if dp[i][j]:
                if i + weight <= a:
                    dp[i + weight][j] = True
                if j + weight <= b:
                    dp[i][j + weight] = True

# 寻找最大总重量
max_w = 0
for i in range(a + 1):
    for j in range(b + 1):
        if dp[i][j]:
            # 更新最大总重量
            if i + j > max_w:
                max_w = i + j

# 输出答案
print(max_w)