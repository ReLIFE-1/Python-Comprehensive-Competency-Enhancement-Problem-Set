def solve():
    l, k = map(int, input().split())
    logs = [int(input()) for _ in range(l)]
    
    def count_ac(n):
        res = 0
        current = 0
        for num in logs:
            current += num
            if current >= n:
                res += 1
                current = 0
            if current < 0:
                current = 0
        return res
    
    # 找最小值
    left = 1
    right = 10**18
    min_n = -1
    while left <= right:
        mid = (left + right) // 2
        cnt = count_ac(mid)
        if cnt > k:
            left = mid + 1
        elif cnt < k:
            right = mid - 1
        else:
            min_n = mid
            right = mid - 1
    
    # 找最大值
    left = 1
    right = 10**18
    max_n = -1
    while left <= right:
        mid = (left + right) // 2
        cnt = count_ac(mid)
        if cnt > k:
            left = mid + 1
        elif cnt < k:
            right = mid - 1
        else:
            max_n = mid
            left = mid + 1
    
    if min_n == -1 or max_n == -1:
        print(-1)
    else:
        print(min_n, max_n)

solve()