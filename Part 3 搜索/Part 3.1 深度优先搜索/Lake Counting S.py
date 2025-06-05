N, M = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(input()))

# 八个方向的偏移量
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(r, c):
    # 将当前'W'标记为'.'，表示已访问
    grid[r][c] = '.'
    
    # 遍历八个方向
    for i in range(8):
        nr, nc = r + dr[i], c + dc[i]    
        # 检查新坐标是否在网格范围内且是'W'
        if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 'W':
            dfs(nr, nc)

pond_count = 0
for r in range(N):
    for c in range(M):
        # 如果当前单元格是'W'，说明找到了一个新的水塘
        if grid[r][c] == 'W':
            pond_count += 1
            dfs(r, c) # 从当前'W'开始，标记所有相连的'W'

print(pond_count)