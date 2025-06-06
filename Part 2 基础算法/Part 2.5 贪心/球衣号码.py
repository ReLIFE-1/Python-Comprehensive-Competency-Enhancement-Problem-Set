# [蓝桥杯 2024 国 Python B] 球衣号码
n, m = map(int, input().split())
p = list(map(int, input().split()))

min_p_idx = min(p)-1
max_p_idx = max(p)-1

maxp = [0] * n

for i in range(n):
    # 最大球衣号码是到最左边队长或最右边队长距离的较大值
    maxp[i] = max(abs(i - min_p_idx), abs(i - max_p_idx))

print(*(maxp))