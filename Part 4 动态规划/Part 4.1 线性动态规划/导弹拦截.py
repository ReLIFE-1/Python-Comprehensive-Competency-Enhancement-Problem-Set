import bisect

nums = list(map(int, input().split()))
n = len(nums)
if n == 0:
    print(0)
    print(0)
    exit()

# === 第一问：最长不上升子序列（非严格递减， >=） ===
tails1 = []
for num in nums:
    # 找到第一个 < num 的位置（bisect_right 的反方向）
    idx = bisect.bisect_right(tails1, -num, 0, len(tails1))
    if idx == len(tails1):
        tails1.append(-num)
    else:
        tails1[idx] = -num
ans1 = len(tails1)

# === 第二问：最少不上升子序列划分数（等价于最长严格上升子序列） ===
tails2 = []
for num in nums:
    idx = bisect.bisect_left(tails2, num)
    if idx == len(tails2):
        tails2.append(num)
    else:
        tails2[idx] = num
ans2 = len(tails2)

print(ans1)
print(ans2)