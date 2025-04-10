def min_m(a):
    max_val = a[-1]
    dp = [False] * (max_val + 1)
    dp[0] = True
    res = 0
    for num in a:
        if not dp[num]:
            res += 1
            for j in range(num, max_val + 1):
                if dp[j - num]:
                    dp[j] = True
    print(res)

T = int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    min_m(a)


