n = int(input())
s = list(map(int, input().split()))
a = list(map(int, input().split()))

# 1. 将房屋信息打包并按推销疲劳值 a 从大到小排序
v = sorted(zip(s, a), key=lambda x: -x[1])

# 2. 预处理数组
sum_a = [0] * (n + 1)  # A值前 i 大的房屋的推销疲劳总和
q = [0] * (n + 1)      # A值前 i 大的房屋中，最大的 2*S 值
h = [0] * (n + 2)      # A值排名从 i 开始的房屋中，最大的 2*S+A 值

# 计算 A 值的前缀和
for i in range(1, n + 1):
    sum_a[i] = sum_a[i - 1] + v[i - 1][1]

# 计算 2*S 的前缀最大值
for i in range(1, n + 1):
    q[i] = max(q[i - 1], 2 * v[i - 1][0])

# 计算 2*S+A 的后缀最大值
for i in range(n, 0, -1):
    h[i] = max(h[i + 1], 2 * v[i - 1][0] + v[i - 1][1])

# 3. 对每个 X (这里用 i 表示) 计算并输出结果
for i in range(1, n + 1):
    # 策略一：选择A值最高的i个房屋
    ans1 = sum_a[i] + q[i]
    
    # 策略二：选择A值最高的i-1个房屋，外加一个能使2S+A最大化的房屋
    ans2 = sum_a[i - 1] + h[i]
    
    # 输出两种策略中的更优结果
    print(max(ans1, ans2))