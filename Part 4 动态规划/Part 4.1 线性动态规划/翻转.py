# [蓝桥杯 2023 国 Python B] 翻转
n = int(input())

if n == 1:
    input()
    print(2)
else:
    # 读取第一个工件
    s_prev = input()
    
    # dp0: 上一个工件不翻转的最小总长度
    # dp1: 上一个工件翻转的最小总长度
    dp0 = 2
    dp1 = 2
    
    # 遍历从第二个到第 n 个工件
    for _ in range(n - 1):
        s_curr = input()
        
        # 计算当前工件不翻转时的最小总长度
        # 它可以从上一个工件不翻转或翻转两种状态转移而来
        cost_from_0 = dp0 + (1 if s_prev[1] == s_curr[0] else 2)
        cost_from_1 = dp1 + (1 if s_prev[0] == s_curr[0] else 2)
        new_dp0 = min(cost_from_0, cost_from_1)
        
        # 计算当前工件翻转时的最小总长度
        cost_from_0_rev = dp0 + (1 if s_prev[1] == s_curr[1] else 2)
        cost_from_1_rev = dp1 + (1 if s_prev[0] == s_curr[1] else 2)
        new_dp1 = min(cost_from_0_rev, cost_from_1_rev)
        
        # 更新状态，为下一次迭代做准备
        dp0 = new_dp0
        dp1 = new_dp1
        s_prev = s_curr

    print(min(dp0, dp1))