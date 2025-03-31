a, b, c, d = map(float, input().split())  # 读取四个系数
roots = []

def f(x):
    return a * x**3 + b * x**2 + c * x + d  # 定义多项式函数

x = -100.0  # 修正：扫描区间从 -100 开始
while x <= 100.0:
    y1 = f(x)
    y2 = f(x + 1.0)
    if y1 * y2 <= 0:
        left = x
        right = x + 1.0
        for _ in range(100):
            mid = (left + right) / 2
            ym = f(mid)
            if y1 * ym <= 0:
                right = mid
                y2 = ym
            else:
                left = mid
                y1 = ym
        root = (left + right) / 2
        roots.append(root)
    x += 1.0  # 以步长 1.0 递增

# 处理根：四舍五入、去重、排序
roots = sorted(list(set([round(r, 2) for r in roots])))
print(' '.join(['{:.2f}'.format(r) for r in roots]))
