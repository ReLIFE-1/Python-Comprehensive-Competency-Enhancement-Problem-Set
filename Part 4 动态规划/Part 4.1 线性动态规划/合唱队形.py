n = int(input())
heights = list(map(int, input().split()))
left = [1] * n  # left[i]表示以i结尾的最长递增子序列的长度
right = [1] * n  # right[i]表示以i开头的最长递减子序列的长度

# 计算left数组
for i in range(n):
    for j in range(i):
        if heights[j] < heights[i] and left[j] + 1 > left[i]:
            left[i] = left[j] + 1

# 计算right数组
for i in range(n-1, -1, -1):
    for j in range(i+1):
        if j < n and heights[j] > heights[i] and right[j] + 1 > right[i]:
            right[i] = right[j] + 1

max_len = 0
for i in range(n):
    current = left[i] + right[i] - 1
    if current > max_len:
        max_len = current

print(n - max_len)