def fast_pow(a, b, p):
    result = 1
    a = a % p  # 防止 a 过大
    while b > 0:
        if b % 2 == 1:  # 如果当前位是 1
            result = (result * a) % p  # 累加到结果中
        a = (a * a) % p  # a 平方
        b = b // 2  # 右移一位
    return result


a, b, p = map(int, input().split())
print(f"{a}^{b} mod {p}={fast_pow(a,b,p)}")
'''
python直接使用内置函数pow(a,b,p)
'''