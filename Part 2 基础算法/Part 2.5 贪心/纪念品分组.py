w = int(input())
n = int(input())
p = [int(input()) for _ in range(n)]
p.sort()

left = 0
right = n - 1
ans = 0

while left <= right:  # 这里改为<=，处理奇数个物品的情况
    if p[left] + p[right] <= w:
        left += 1      
    right -= 1         
    ans += 1

print(ans)