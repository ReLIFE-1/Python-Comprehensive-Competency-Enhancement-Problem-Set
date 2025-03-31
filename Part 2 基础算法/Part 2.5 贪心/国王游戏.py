n = int(input())
king = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]

a.sort(key=lambda x: x[0] * x[1])
s = king[0]
max_val = 0

for i in range(n):
    p = s // a[i][1]
    if p > max_val:
        max_val = p
    s *= a[i][0]

print(max_val)