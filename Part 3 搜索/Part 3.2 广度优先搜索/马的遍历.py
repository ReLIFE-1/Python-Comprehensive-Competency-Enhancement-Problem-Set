def bfs(n, m, x, y):
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]
    visited[x-1][y-1] = 0
    queue = [(x-1, y-1)]
    
    while queue:
        cx, cy = queue.pop(0)
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                visited[nx][ny] = visited[cx][cy] + 1
                queue.append((nx, ny))
    
    for row in visited:
        print(' '.join(map(str, row)))

n, m, x, y = map(int, input().split())
bfs(n, m, x, y)