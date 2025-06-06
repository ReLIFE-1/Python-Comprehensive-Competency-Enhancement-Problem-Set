import math

# 欧几里得算法求最大公约数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 获取一个数的所有不重复的质因子
def get_distinct_prime_factors(n):
    factors = set()
    d = 2
    temp_n = n
    while d * d <= temp_n:
        if temp_n % d == 0:
            factors.add(d)
            while temp_n % d == 0:
                temp_n //= d
        d += 1
    if temp_n > 1:
        factors.add(temp_n)
    return list(factors)

# 计算欧拉函数 phi(n)
def phi(n, factors):
    res = n
    for p in factors:
        res = res // p * (p - 1)
    return res

# 获取一个数的所有因子
def get_divisors(n):
    divs = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return sorted(list(divs))

def solve():
    n = int(input())
    MOD = 998244353

    min_k = float('inf')
    best_d = -1

    for d in range(1, 10):
        val = 9 * n
        common = gcd(d, val)
        m = val // common

        if m % 2 == 0 or m % 5 == 0:
            continue

        if m == 1: # 10^k mod 1 = 0 != 1. 但k=1时，(10-1)/9=1, d*1 % n, 这种情况需要k=phi(m)=1
            k = 1
        else:
            prime_factors_m = get_distinct_prime_factors(m)
            phi_m = phi(m, prime_factors_m)
            divs = get_divisors(phi_m)
            
            # 找到最小的 k
            for p in divs:
                if pow(10, p, m) == 1:
                    k = p
                    break
        
        # 更新最优解
        if k < min_k:
            min_k = k
            best_d = d
        elif k == min_k and d < best_d:
            best_d = d

    if best_d == -1:
        print(-1)
    else:
        # 计算 (d * (10^k - 1) / 9) % MOD
        k = min_k
        d = best_d
        
        # 计算 9 的模逆元
        inv9 = pow(9, MOD - 2, MOD)
        
        term1 = d
        term2 = (pow(10, k, MOD) - 1 + MOD) % MOD # type: ignore
        
        ans = (term1 * term2) % MOD
        ans = (ans * inv9) % MOD
        
        print(ans)

solve()