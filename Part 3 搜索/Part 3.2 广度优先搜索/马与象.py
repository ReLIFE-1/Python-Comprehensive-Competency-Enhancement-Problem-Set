# [蓝桥杯 2024 国 Python B] 马与象
from collections import deque

def bfs(N, x, y, moves):
    dist = [[-1] * (N + 1) for _ in range(N + 1)]
    q = deque()
    q.append((x, y))
    dist[x][y] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy 
            if 0 <= nx <= N and 0 <= ny <= N and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist

N, x1, y1, x2, y2 = map(int, input().split())
hd = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),(1, -2), (1, 2), (2, -1), (2, 1)]
ed = [(-2, -2), (-2, 2), (2, -2), (2, 2)]

# 分别计算到棋盘各点的最短步数
hs = bfs(N, x1, y1, hd)
es = bfs(N, x2, y2, ed)

min_step = -1

for i in range(N + 1):
    for j in range(N + 1):
        # 如果马和象都能到达 (i, j)
        if hs[i][j] != -1 and es[i][j] != -1:
            cs = hs[i][j] + es[i][j]
            # 更新最小总步数
            if min_step == -1 or cs < min_step:
                min_step = cs

print(min_step)