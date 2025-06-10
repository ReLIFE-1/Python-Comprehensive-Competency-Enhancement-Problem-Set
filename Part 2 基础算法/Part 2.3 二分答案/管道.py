import math

def solve():
    n, pipe_len = map(int, input().split())
    valves = []
    for _ in range(n):
        l, s = map(int, input().split())
        valves.append((l, s))

    def check(t):
        if t < 0:
            return False
            
        intervals = []
        for l, s in valves:
            if t >= s:
                # 计算水流扩散的距离
                d = t - s
                # 计算覆盖的区间，并与管道范围 [1, pipe_len] 取交集
                start = max(1, l - d)
                end = min(pipe_len, l + d)
                intervals.append((start, end))
        
        # 如果没有任何阀门开启，则无法覆盖
        if not intervals:
            return False
        
        # 按区间的起始位置排序
        intervals.sort()
        
        # 检查管道的起始位置 1 是否被覆盖
        if intervals[0][0] > 1:
            return False
        
        # 合并区间并检查连续性
        max_reach = intervals[0][1]
        
        # 如果第一个区间就能覆盖全部，直接返回 True
        if max_reach >= pipe_len:
            return True
            
        for i in range(1, len(intervals)):
            # 如果当前区间和已覆盖区域之间有空隙
            if intervals[i][0] > max_reach + 1:
                return False
            # 更新最大覆盖范围
            max_reach = max(max_reach, intervals[i][1])
            # 如果已完全覆盖，提前结束
            if max_reach >= pipe_len:
                return True
                
        return max_reach >= pipe_len

    # 二分查找答案
    left = 0
    # 一个足够大的上界，例如最晚的阀门开启时间 + 管道长度
    right = 2 * 10**9 
    ans = right

    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            # mid 时间可行，尝试更早的时间
            ans = mid
            right = mid - 1
        else:
            # mid 时间不可行，需要更晚的时间
            left = mid + 1
            
    print(ans)

solve()