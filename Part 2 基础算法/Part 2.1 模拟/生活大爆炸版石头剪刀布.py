# 读取输入
N, N_A, N_B = map(int, input().split())
A_sequence = list(map(int, input().split()))
B_sequence = list(map(int, input().split()))

# 定义每个手势可以击败的手势
# 0: 剪刀, 1: 石头, 2: 布, 3: 蜥蜴人, 4: 斯波克
win_map = {
    0: [2, 3],  # 剪刀胜布和蜥蜴人
    1: [0, 3],  # 石头胜剪刀和蜥蜴人
    2: [1, 4],  # 布胜石头和斯波克
    3: [4, 2],  # 蜥蜴人胜斯波克和布
    4: [0, 1],  # 斯波克胜剪刀和石头
}

# 初始化得分
A_score = 0
B_score = 0

# 进行N次对战
for i in range(N):
    A_move = A_sequence[i % N_A]
    B_move = B_sequence[i % N_B]
    if A_move == B_move:
        continue  # 平局，双方都得0分
    elif B_move in win_map[A_move]:
        A_score += 1  # A获胜
    else:
        B_score += 1  # B获胜

# 输出结果
print(A_score, B_score)