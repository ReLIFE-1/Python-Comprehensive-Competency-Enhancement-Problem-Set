n = int(input())
matrix = [[0]*n for _ in range(n)]
for i in range(n-1):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        matrix[i][i+1+j] = row[j]
        matrix[i+1+j][i] = row[j]

max_second = 0
for i in range(n):
    row = matrix[i]
    first_max = max(row)
    # 获取第二大的值
    sorted_row = sorted(row, reverse=True)
    second_max = sorted_row[1]
    if second_max > max_second:
        max_second = second_max

print(1)
print(max_second)