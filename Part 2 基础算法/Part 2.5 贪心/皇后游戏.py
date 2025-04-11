T = int(input())

for _ in range(T):
    n = int(input())

    group_a = []
    group_b = []
    # 读取大臣数据并直接分组
    for i in range(n):
        a, b = map(int, input().split())
        if a < b:
            group_a.append((a, b))
        else:
            group_b.append((a, b))

    # A组按 a 升序, B组按 b 降序
    group_a.sort(key=lambda x: x[0])
    group_b.sort(key=lambda x: x[1], reverse=True)

    # 得到最优排序
    final_order = group_a + group_b

    # 计算最大奖金
    sum_a = 0
    c_prev = 0
    max_c = 0
    for a, b in final_order:
        sum_a = sum_a + a
        # c_i = max(c_{i-1}, sum_a) + b_i
        c_curr = max(c_prev, sum_a) + b
        max_c = max(max_c, c_curr)
        c_prev = c_curr
    
    print(max_c)