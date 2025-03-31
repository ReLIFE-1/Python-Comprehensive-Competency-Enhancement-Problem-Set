def S(a1,a2,n):
    d = a2 - a1
    return a1 * n + n*(n-1)//2 * d

a1,a2,n = map(int,input().split())
print(S(a1,a2,n))
