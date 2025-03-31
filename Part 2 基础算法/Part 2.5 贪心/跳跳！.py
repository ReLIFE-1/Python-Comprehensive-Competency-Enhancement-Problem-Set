n = int(input())
rocks = list(map(int,input().split()))
rocks.sort()
left ,right = 0,n - 1
cur,cost = 0,0
jump_high = True
while left <= right:
    if jump_high:
        cost += (rocks[right] - cur) ** 2
        cur = rocks[right]
        right -= 1
    else:
        cost += (rocks[left] - cur) ** 2
        cur = rocks[left]
        left += 1
    jump_high = not jump_high
print(cost)

