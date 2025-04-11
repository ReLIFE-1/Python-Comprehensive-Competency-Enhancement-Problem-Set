def count_cells(n, m, cells):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    visited = [[False] * m for _ in range(n)]
    
    def bfs(start_x, start_y):
        queue = [(start_x, start_y)]
        visited[start_x][start_y] = True
        
        while queue:
            x, y = queue.pop(0)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and cells[nx][ny] != '0':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    cell_count = 0
    
    for i in range(n):
        for j in range(m):
            if cells[i][j] != '0' and not visited[i][j]:
                bfs(i, j)
                cell_count += 1
    
    return cell_count

n, m = map(int, input().split())
cells = [input().strip() for _ in range(n)]

print(count_cells(n, m, cells))