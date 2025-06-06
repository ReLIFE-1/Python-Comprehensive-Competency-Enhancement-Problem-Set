# [蓝桥杯 2024 国 Python B] 工厂
n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))

# 使用邻接表来存储生产关系
# adj[y] 存储所有能生产物品 y 的方式，每个方式为一个元组 (x, k, w)
adj = [[] for _ in range(n + 1)]

# 读取 m 种生产方式
for _ in range(m):
    x, y, k, w = map(int, input().split())
    # 如果 k=0，表示是第一类生产方式，为了统一，我们将原材料 x 记为 0
    if k == 0:
        adj[y].append((0, k, w))
    else:
        adj[y].append((x, k, w))

# cost[i] 存储生产一个单位物品 i 所需的最小工人天数
# 初始化为无穷大
cost = [float('inf')] * (n + 1)

# 按物品编号 1 到 n 的顺序计算成本
for i in range(1, n + 1):
    # 遍历所有可以生产物品 i 的方式
    for x, k, w in adj[i]:
        current_cost = float('inf')
        if k == 0:
            # 第一类生产：1个工人天产出 w 件，单位成本为 1/w
            current_cost = 1 / w
        else:
            # 第二类生产：需要先获得原材料 x
            # 如果原材料 x 的成本已知（不是无穷大）
            if cost[x] != float('inf'):
                # 总成本 = 原材料成本 + 1个加工工人天
                # 单位成本 = 总成本 / 产出数量
                current_cost = (k * cost[x] + 1) / w
        
        # 更新物品 i 的最小成本
        cost[i] = min(cost[i], current_cost)

# 初始化最大平均收益为 0
max_profit = 0.0

# 遍历所有物品，计算并找到最大收益
for i in range(1, n + 1):
    # 如果物品 i 可以出售 (a[i] > 0) 并且可以生产 (cost[i] is not inf)
    if a[i] > 0 and cost[i] != float('inf'):
        # 计算该物品的平均收益，并更新最大值
        profit = a[i] / cost[i]
        if profit > max_profit:
            max_profit = profit

# 按格式要求输出，保留两位小数
print(f"{max_profit:.2f}")