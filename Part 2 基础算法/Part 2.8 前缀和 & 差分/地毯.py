n,m = map(int,input().split())
a = [[0]*(n+2) for _ in range(n+2)]

def insert(x1,y1,x2,y2):
    a[x1][y1] += 1
    a[x1][y2+1] -= 1
    a[x2+1][y1] -= 1
    a[x2+1][y2+1] += 1

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    insert(x1, y1, x2, y2)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        a[i][j] += a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1]

for i in range(1, n + 1):
    print(' '.join(map(str, a[i][1:n+1])))