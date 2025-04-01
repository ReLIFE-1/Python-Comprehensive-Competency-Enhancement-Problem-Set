n, x = map(int, input().split())
H = [0]+list(map(int, input().split()))

# 计算前缀和
prefix = [0] * (n+1)
for i in range(1, n):
    prefix[i] = prefix[i - 1] + H[i]

left = 1
right = n
ans = n

# 检查y是否可以作为答案
def is_possible(y):
    # 检查所有长度为y的窗口的和是否>=2x
    for i in range(n - y):
        current_sum = prefix[i + y] - prefix[i]
        if current_sum < 2 * x:
            return False
    return True

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)