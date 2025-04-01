n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

if n == 1:
    print(0)
    print(1)
    exit()

diff = []
for i in range(1, n):
    diff.append(a[i] - a[i-1])

pos = 0
neg = 0
for num in diff:
    if num > 0:
        pos += num
    elif num < 0:
        neg += num

min_operations = max(pos, -neg)
num_results = abs(pos + neg) + 1

print(min_operations)
print(num_results)