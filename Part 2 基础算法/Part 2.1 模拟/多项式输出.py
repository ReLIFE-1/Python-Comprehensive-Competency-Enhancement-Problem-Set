n = int(input())
coefficients = list(map(int, input().split()))
result = ""
for i in range(n + 1):
    coef = coefficients[i]
    power = n - i
    if coef == 0:
        continue
    if not result:
        if coef < 0:
            result += "-"
    else:
        if coef > 0:
            result += "+"
        else:
            result += "-"
    abs_coef = abs(coef)
    if abs_coef != 1 or power == 0:
        result += str(abs_coef)
    if power > 0:
        result += "x"
        if power > 1:
            result += "^" + str(power)
print(result if result else "0")