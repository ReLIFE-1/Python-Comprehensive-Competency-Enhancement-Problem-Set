n, m = map(int, input().split())
queue = list(range(1, n + 1))  # 初始化队列，编号1到n
result = []                    # 保存出圈顺序
index = 0                      # 当前指针位置

while len(queue) > 0:
    index = (index + m - 1) % len(queue)  # 找到需要出圈的人的位置
    result.append(str(queue.pop(index)))  # 出圈，并记录编号

print(' '.join(result))