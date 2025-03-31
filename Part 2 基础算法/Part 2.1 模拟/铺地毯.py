n = int(input())
blankets = []
for i in range(n):
    a, b, g, k = map(int, input().split())
    blankets.append([a, b, g, k])

x, y = map(int, input().split())
res = -1

# 从最后一张地毯开始检查
for i in range(n-1, -1, -1):
    a, b, g, k = blankets[i]
    if a <= x <= a + g and b <= y <= b + k:
        res = i + 1  # 编号从1开始
        break

print(res)
