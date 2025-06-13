m, s, t = map(int, input().split())

dist_f = 0
dist_r = 0

for i in range(1, t + 1):
    
    # 1. 决策与移动
    if m >= 10:
        # 魔力充足，闪烁策略前进60，跑步策略前进17
        m -= 10
        dist_f += 60
        dist_r += 17
    else:
        # 魔力不足，闪烁策略休息回蓝
        m += 4
        # 跑步策略的核心：如果落后了，就先同步到闪烁策略的进度
        if dist_f > dist_r:
            dist_r = dist_f
        # 然后再前进17
        dist_r += 17

    # 2. 判断是否逃脱
    # 守望者的实际最远距离是两种策略中的最大值
    if max(dist_f, dist_r) >= s:
        print("Yes")
        print(i)
        exit() # 成功逃脱，直接退出程序

# 3. 如果循环结束仍未逃脱
print("No")
print(max(dist_f, dist_r))