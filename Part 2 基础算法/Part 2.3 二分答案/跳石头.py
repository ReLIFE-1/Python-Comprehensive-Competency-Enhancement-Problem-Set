L, N, M = map(int, input().split())
rocks = [int(input()) for _ in range(N)]

rocks.append(L) # 将终点L添加到岩石列表中，方便统一处理跳跃距离

left, right = 1, L # 二分查找的左右边界，最短跳跃距离的可能范围是1到L
result = 0 # 存储最终的最大最短跳跃距离

while left <= right:
    mid = (left + right) // 2 # 尝试以mid作为最短跳跃距离
    removed = 0 # 记录需要移除的岩石数量
    prev = 0 # 当前跳跃的起点位置，初始为0（比赛起点）
    
    # 遍历所有岩石（包括终点L）来计算在当前mid下需要移除多少岩石
    for rock in rocks:
        if rock - prev < mid: # 如果从当前起点到下一块岩石的距离小于mid
            removed += 1 # 那么这块岩石必须被移除
            if removed > M: # 如果移除数量已经超过M，说明mid不可行，直接跳出
                break
        else: # 如果距离大于等于mid，可以跳到这块岩石上
            prev = rock # 更新当前跳跃起点
            
    if removed <= M: # 如果在当前mid下，移除的岩石数量没有超过M
        result = mid # 说明mid是可行的，记录下来，并尝试更大的最短距离
        left = mid + 1
    else: # 如果移除数量超过M，说明mid太大，需要减小最短距离
        right = mid - 1

print(result)