import itertools
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n,k = map(int,input().split())
a = list(map(int,input().split()))
cnt = 0

for comb in itertools.combinations(a,k): # 生成k个数的组合
    s = sum(comb)
    if is_prime(s):
        cnt += 1

print(cnt)