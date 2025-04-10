r,c = map(int,input().split())
sea = [input().strip() for _ in range(r)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * c for _ in range(r)]
def is_valid(x, y):
    return 0 <= x < r and 0 <= y < c and not visited[x][y] and sea[x][y] == '#'

def dfs(x,y):
    visited[x][y] = True
    for dx,dy in directions:
        nx,ny = x + dx,y + dy
        if is_valid(nx,ny):
            dfs(nx,ny)

def count_ships():
    cnt = 0
    for i in range(r):
        for j in range(c):
            if is_valid(i, j):
                dfs(i, j)
                cnt += 1
    return cnt   

print(f'There are {count_ships()} ships.')