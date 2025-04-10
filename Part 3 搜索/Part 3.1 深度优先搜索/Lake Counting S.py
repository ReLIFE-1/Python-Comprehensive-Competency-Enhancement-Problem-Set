n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

# 用于标记访问过的方格
visited = [[False] * m for _ in range(n)]

# 方向向量，表示一个方格的八个可能邻居
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def is_valid(x, y):
    """ 检查坐标是否在矩阵范围内,并且未访问且是水(‘W’) """
    return 0 <= x < n and 0 <= y < m and not visited[x][y] and field[x][y] == 'W'

def dfs(x, y):
    """ 深度优先搜索标记当前水塘 """
    # 标记当前方格为已访问
    visited[x][y] = True
    # 检查所有邻居方格
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny):
            dfs(nx, ny)

def count_lakes():
    lakes_count = 0
    # 遍历矩阵的所有方格
    for i in range(n):
        for j in range(m):
            # 如果找到一个未访问过的水方格，开始新的DFS
            if is_valid(i, j):
                dfs(i, j)
                # 每次完成 DFS 意味着完成一个水塘的标记
                lakes_count += 1
    return lakes_count

print(count_lakes())