from collections import deque
N = int(input())

H = []
for _ in range(N):
    H.append(list(map(int, input().split())))

# 初始化距离数组，所有距离设置为无穷大
dist = [[float('inf')] * N for _ in range(N)]
dist[0][0] = 0

# 初始化队列，将起点加入队列
q = deque([(0, 0)])

# BFS
while q:
    r, c = q.popleft()

    # 移动方式 1: 向下移动
    if r + 1 < N:
        if dist[r][c] + 1 < dist[r + 1][c]:
            dist[r + 1][c] = dist[r][c] + 1
            q.append((r + 1, c))

    # 移动方式 2: 向右移动
    if c + 1 < N:
        if dist[r][c] + 1 < dist[r][c + 1]:
            dist[r][c + 1] = dist[r][c] + 1
            q.append((r, c + 1))

    # 移动方式 3: 向右跳跃
    # 当前方格的高度 H[r][c] 必须大于下一个方格
    if c + 1 < N and H[r][c] > H[r][c+1]:
        # 从 (r, c+1) 开始向右遍历
        for L in range(1, N - c):
            if c + L < N and H[r][c + L - 1] > H[r][c + L]:
                if dist[r][c] + 1 < dist[r][c + L]:
                    dist[r][c + L] = dist[r][c] + 1
                    q.append((r, c + L))
            else: # 不满足递减条件，停止向右跳跃
                break

# 输出到终点的最短时间
print(dist[N - 1][N - 1])