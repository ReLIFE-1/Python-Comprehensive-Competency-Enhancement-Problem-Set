# [蓝桥杯 2025 省 Python B] 园艺

import sys

n = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))

# 如果树的数量小于等于2，直接输出n
if n <= 2:
    print(n)
else:
    # dp[i][j]表示以索引j和i结尾的等间隔递增序列的最大长度
    dp = [[0] * n for _ in range(n)]
    
    # 至少可以留下一棵树，所以最大长度至少为1
    max_len = 1
    
    # i是序列最后一个元素的索引
    for i in range(n):
        # j是序列倒数第二个元素的索引
        for j in range(i):
            # 必须满足高度递增
            if h[j] < h[i]:
                # 默认长度为2，即只有h[j]和h[i]两棵树
                length = 2
                
                # 计算公差
                diff = i - j
                # 找到j之前的那个元素的索引k
                k = j - diff
                
                # 如果k存在且合法
                if k >= 0:
                    # 如果以k,j结尾的序列存在，则在此基础上加1
                    if dp[j][k] > 0:
                        length = dp[j][k] + 1
                
                dp[i][j] = length
                
                # 更新最大长度
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    
    print(max_len)