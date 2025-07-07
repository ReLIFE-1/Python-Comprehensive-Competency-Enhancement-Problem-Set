# 读入牛棚数量 N
n = int(input())

# 使用列表存储每个牛棚的下一个目的地，索引从1开始
# 为了方便处理1到N的索引，列表大小设为 N+1
next_node = [0] * (n + 1)
for i in range(1, n + 1):
    next_node[i] = int(input())

# ans 列表用于存储每个牛棚出发的最终步数
ans = [0] * (n + 1)

# 遍历所有牛棚
for i in range(1, n + 1):
    # 如果当前牛棚的答案尚未计算
    if ans[i] == 0:
        # 开始追踪路径
        path = []
        curr = i
        
        # 循环直到遇到一个已经计算过答案的节点或形成环路
        while ans[curr] == 0:
            # 将当前节点加入本次遍历的路径
            path.append(curr)
            # 标记当前节点为“正在访问”（用-1表示）
            ans[curr] = -1
            # 前往下一个节点
            curr = next_node[curr]

        # 检查停止的原因
        # 情况1：形成环路 (下一个节点是“正在访问”的节点)
        if ans[curr] == -1:
            # 找到环的起点在路径中的索引
            cycle_start_index = path.index(curr)
            # 计算环的长度
            cycle_len = len(path) - cycle_start_index
            
            # 环上所有节点的答案都是环的长度
            for j in range(cycle_start_index, len(path)):
                ans[path[j]] = cycle_len
            
            # 计算通向环的“尾巴”路径上节点的答案
            l = cycle_len
            for j in range(cycle_start_index - 1, -1, -1):
                l += 1
                ans[path[j]] = l
        
        # 情况2：汇入已知路径 (下一个节点的答案已经计算过)
        else:
            l = ans[curr]
            # 从后往前遍历当前路径，计算每个节点的答案
            for node in reversed(path):
                l += 1
                ans[node] = l

# 逐行输出每个牛棚的答案
for i in range(1, n + 1):
    print(ans[i])