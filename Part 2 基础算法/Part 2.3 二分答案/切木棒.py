n, m = map(int, input().split())
L = list(map(int, input().split()))

def check(x):
    # 计算当最长木棒长度不超过x时，需要切多少次
    cuts = 0
    for l in L:
        # 如果木棒长度l大于x，就需要切
        if l > x:
            # 实际切的次数是 段数 - 1
            cuts += int(l / x)
    return cuts

# 二分查找的范围
low = 1
high = max(L) + 1 
ans = high 

while low < high:
    mid = low + (high - low) // 2
    if check(mid) <= m:
        ans = mid
        high = mid
    else:
        low = mid + 1

print(ans)