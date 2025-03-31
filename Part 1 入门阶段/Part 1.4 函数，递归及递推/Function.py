# 预先计算w(a,b,c)的值
dp = [[[0 for _ in range(21)] for __ in range(21)] for ___ in range(21)]

for a in range(21):
    for b in range(21):
        for c in range(21):
            if a == 0 or b == 0 or c == 0:
                dp[a][b][c] = 1
            elif a < b and b < c:
                dp[a][b][c] = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
            else:
                dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]

while True:
    try:
        a, b, c = map(int, input().split())
        if a == -1 and b == -1 and c == -1:
            break
        if a <= 0 or b <= 0 or c <= 0:
            ans = 1
        elif a > 20 or b > 20 or c > 20:
            ans = dp[20][20][20]
        elif a < b and b < c:
            ans = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
        else:
            ans = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]
        print(f"w({a}, {b}, {c}) = {ans}")
    except EOFError:
        break
