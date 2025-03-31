n,m = map(int,input().split())
milk = []
for _ in range(m):
    milk.append(list(map(int,input().split())))
milk.sort(key = lambda x:x[0])
cost = 0
for m in milk:
    if n > m[1]:
        cost += m[0] * m[1]
        n -= m[1]
    else:
        cost += m[0] * n
        break

print(cost)
    


