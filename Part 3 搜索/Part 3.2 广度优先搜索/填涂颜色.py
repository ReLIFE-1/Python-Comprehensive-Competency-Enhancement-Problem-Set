n = int(input())
grid = []
visited = [[False for _ in range(n)] for _ in range(n)]
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# 方向数组，上下左右
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

from collections import deque

# 处理边界上的0，并开始BFS
q = deque()
for i in range(n):
    for j in range(n):
        if (i == 0 or i == n-1 or j == 0 or j == n-1) and grid[i][j] == 0:
            visited[i][j] = True
            q.append((i, j))

# BFS标记所有可以从边界到达的0
while q:
    x, y = q.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny))

# 将未被标记的0替换为2
for i in range(n):
    for j in range(n):
        if grid[i][j] == 0 and not visited[i][j]:
            grid[i][j] = 2

# 输出结果
for row in grid:
    print(' '.join(map(str, row)))