n = int(input())
mod = 7
prefix = [0] * (n + 1)
first_occurrence = [-1] * mod
first_occurrence[0] = 0  # 处理前缀和模7余0的情况，即从0开始的子串
max_len = 0

for i in range(1, n + 1):
    num = int(input())
    prefix[i] = (prefix[i - 1] + num) % mod
    # 记录余数的首次出现位置
    if first_occurrence[prefix[i]] == -1:
        first_occurrence[prefix[i]] = i
    else:
        # 如果之前出现过，则更新最大长度
        current_len = i - first_occurrence[prefix[i]]
        if current_len > max_len:
            max_len = current_len

print(max_len)

