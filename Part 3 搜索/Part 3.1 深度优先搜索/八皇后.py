n = int(input())
col = [False] * (n + 1)          # 标记列是否被占用
diag1 = [False] * (2 * n + 1)        # 主对角线 (行 + 列)
diag2 = [False] * (2 * n + 1)        # 副对角线 (行 - 列 + n)
result = []                      # 存储所有解

def dfs(row, queens):
    if row > n:                  # 找到可行解
        result.append(queens.copy())
        return
    for c in range(1, n + 1):
        if not col[c] and not diag1[row + c] and not diag2[row - c + n]:
            queens.append(c)
            col[c] = diag1[row + c] = diag2[row - c + n] = True
            dfs(row + 1, queens)  # 递归下一行
            # 回溯
            queens.pop()
            col[c] = diag1[row + c] = diag2[row - c + n] = False

dfs(1, [])
for solution in result[:3]:
    print(' '.join(map(str, solution)))
print(len(result))