n = int(input())
intervals = []
max_y = 0
for _ in range(n):
    x, y = map(int, input().split())
    intervals.append((x, y))
    if y > max_y:
        max_y = y

# 按照右端点排序
intervals.sort(key=lambda x: x[1])

# dp数组，最大到max_y
dp = [0] * (max_y + 2)

it = 0
# 遍历每一个可能的位置
for current_y in range(1, max_y + 1):
    dp[current_y] = dp[current_y - 1]
    # 处理所有右端点等于current_y的区间
    while it < n and intervals[it][1] == current_y:
        x, y = intervals[it]
        temp = dp[x - 1] + (y - x + 1)
        if temp > dp[current_y]:
            dp[current_y] = temp
        it += 1

print(dp[max_y])