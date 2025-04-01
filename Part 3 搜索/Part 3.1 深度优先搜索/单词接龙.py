n = int(input())
words = [input().strip() for _ in range(n)]
start_char = input().strip()

# 预处理每个单词对之间的最小重叠长度
overlap = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        a, b = words[i], words[j]
        min_len = min(len(a), len(b))
        for k in range(1, min_len):
            if a.endswith(b[:k]):
                overlap[i][j] = k
                break

max_len = 0
used = [0] * n

# DFS函数，current是当前单词的索引，length是当前龙的长度
def dfs(current, length):
    global max_len
    max_len = max(max_len, length)
    for next_word in range(n):
        if used[next_word] >= 2:
            continue
        if overlap[current][next_word] == 0:
            continue
        used[next_word] += 1
        # 新增长度为 b的长度 - 重叠部分
        added_len = len(words[next_word]) - overlap[current][next_word]
        dfs(next_word, length + added_len)
        used[next_word] -= 1

# 初始化：找到所有以start_char开头的单词作为起点
for i in range(n):
    if words[i][0] == start_char:
        used[i] += 1
        dfs(i, len(words[i]))
        used[i] -= 1

print(max_len)