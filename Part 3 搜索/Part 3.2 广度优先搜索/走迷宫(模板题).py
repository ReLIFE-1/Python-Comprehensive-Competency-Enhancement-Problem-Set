n,m = map(int,input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

def dfs(n,m,maze):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[-1] * (m) for _ in range(n)]
    queue = [(0,0)]
    visited[0][0] = 0
    while queue:
        x,y = queue.pop(0)
        for  i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 0  and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    
    # 返回终点的步数
    return visited[n-1][m-1]

print(dfs(n,m,maze))


