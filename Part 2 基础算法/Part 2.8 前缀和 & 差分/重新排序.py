n = int(input())
A = list(map(int, input().split()))
m = int(input())

# 计算原数组的前缀和
pre = [0] * (n + 1)
for i in range(1, n + 1):
    pre[i] = pre[i-1] + A[i-1]

sum_origin = 0
diff = [0] * (n + 2)  # 使用1-based到n-based的位置
for _ in range(m):
    L,R = map(int, input().split())
    sum_origin += pre[R] - pre[L-1]
    diff[L] += 1
    diff[R + 1] -= 1


# 计算覆盖次数数组cnt
current = 0
cnt = []
for i in range(1, n + 1):
    current += diff[i]
    cnt.append(current)

# 排序并计算最大可能的总和
sorted_A = sorted(A, reverse=True)
sorted_cnt = sorted(cnt, reverse=True)

sum_max = sum(a * c for a, c in zip(sorted_A, sorted_cnt))
print(sum_max - sum_origin)