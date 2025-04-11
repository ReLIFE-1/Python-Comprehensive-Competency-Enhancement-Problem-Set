L, R = map(int, input().split())
count = 0

for num in range(L, R + 1):
    # 将整数转换为字符串，方便逐位检查
    s_num = str(num)
    for char in s_num:
        if char == '2':
            count += 1

print(count)