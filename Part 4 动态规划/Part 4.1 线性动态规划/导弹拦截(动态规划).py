# 洛谷会超时
nums = list(map(int, input().split()))
n = len(nums)
if n == 0:
    print(0)
    print(0)
    exit()

# === 第一问：最长不上升子序列 ===
dp1 = [1] * n  # dp1[i] 表示以 nums[i] 结尾的最长不上升子序列的长度
for i in range(n):
    for j in range(i):
        if nums[j] >= nums[i] and dp1[j] + 1 > dp1[i]:
            dp1[i] = dp1[j] + 1
ans1 = max(dp1)  # 结果为 dp1 中的最大值

# === 第二问：最少需要多少套系统（Dilworth 定理：最长上升序列长度） ===
dp2 = [1] * n  # dp2[i] 表示以 nums[i] 结尾的最长上升子序列的长度
for i in range(n):
    for j in range(i):
        if nums[j] < nums[i] and dp2[j] + 1 > dp2[i]:
            dp2[i] = dp2[j] + 1
ans2 = max(dp2)  # 结果为 dp2 中的最大值

print(ans1)
print(ans2)