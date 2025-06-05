R, C = map(int, input().split())
grid = []
for _ in range(R):
    grid.append(list(input()))

visited = [[False for _ in range(C)] for _ in range(R)]
ships = 0
bad_placement = False

# 定义队列，用于BFS
q = []

for r_start in range(R):
    for c_start in range(C):
        if grid[r_start][c_start] == '#' and not visited[r_start][c_start]:
            ships += 1
            
            min_r, max_r = r_start, r_start
            min_c, max_c = c_start, c_start

            # 将起点加入队列
            q.append((r_start, c_start))
            visited[r_start][c_start] = True

            head = 0 # 模拟队列的头部指针
            while head < len(q):
                curr_r, curr_c = q[head]
                head += 1

                # 更新船只的边界
                min_r = min(min_r, curr_r)
                max_r = max(max_r, curr_r)
                min_c = min(min_c, curr_c)
                max_c = max(max_c, curr_c)

                dr = [-1, 1, 0, 0]
                dc = [0, 0, -1, 1]

                for i in range(4):
                    nr, nc = curr_r + dr[i], curr_c + dc[i]
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '#' and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))
            
            # 清空队列，准备下一个船只的BFS
            q.clear()

            # 检查船只是否为矩形
            for row_check in range(min_r, max_r + 1):
                for col_check in range(min_c, max_c + 1):
                    if grid[row_check][col_check] == '.':
                        bad_placement = True
                        break
                if bad_placement:
                    break
            if bad_placement:
                break
            
            # 检查船只四周八个方向是否有接触
            for row_offset in range(min_r - 1, max_r + 2):
                for col_offset in range(min_c - 1, max_c + 2):
                    # 跳过矩形内部的格子
                    if min_r <= row_offset <= max_r and min_c <= col_offset <= max_c:
                        continue
                    
                    # 检查边界
                    if 0 <= row_offset < R and 0 <= col_offset < C:
                        if grid[row_offset][col_offset] == '#':
                            bad_placement = True
                            break
                if bad_placement:
                    break
            if bad_placement:
                break
    if bad_placement:
        break

if bad_placement:
    print("Bad placement.")
else:
    print(f"There are {ships} ships.")