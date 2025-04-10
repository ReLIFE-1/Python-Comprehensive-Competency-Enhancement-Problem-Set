import sys
from math import hypot

# 读取输入
input = sys.stdin.read
data = input().split()
n = int(data[0])
points = [(float(data[i]), float(data[i+1])) for i in range(1, 2*n, 2)]

# 距离函数
def dist(p1, p2):
    return hypot(p1[0] - p2[0], p1[1] - p2[1])

# 分治核心算法
def closest_pair(px, py):
    n = len(px)
    if n <= 3:
        return min(dist(px[i], px[j]) for i in range(n) for j in range(i + 1, n))
    
    mid = n // 2
    mid_x = px[mid][0]
    left_x = px[:mid]
    right_x = px[mid:]
    left_y = [p for p in py if p[0] <= mid_x]
    right_y = [p for p in py if p[0] > mid_x]

    d1 = closest_pair(left_x, left_y)
    d2 = closest_pair(right_x, right_y)
    d = min(d1, d2)

    strip = [p for p in py if abs(p[0] - mid_x) < d]
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= d:
                break
            d = min(d, dist(strip[i], strip[j]))
    return d

# 主函数
px = sorted(points)
py = sorted(points, key=lambda p: p[1])
result = closest_pair(px, py)

# 输出结果，保留4位小数
print(f"{result:.4f}")
