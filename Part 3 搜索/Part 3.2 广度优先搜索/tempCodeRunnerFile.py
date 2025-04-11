n, m = map(int, input().split())
maze = [input().strip() for _ in range(n)]

def bfs(n, maze, x, y):
    visited = [[False] * n for _ in range(n)]
    queue = []
    queue.append((x - 1, y - 1))
    visited[x - 1][y - 1] = True
    count = 1  # 起点自己也算一个

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        a, b = queue.pop(0)
        current_val = maze[a][b]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and maze[nx][ny] != current_val:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
    return count

for _ in range(m):
    x, y = map(int, input().split())
    print(bfs(n, maze, x, y))
