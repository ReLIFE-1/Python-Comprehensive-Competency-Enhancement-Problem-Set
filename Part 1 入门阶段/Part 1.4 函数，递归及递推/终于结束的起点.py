M = int(input())

fib0, fib1 = 0, 1
for n in range(1, M * M + 1):
    fib_next = (fib0 + fib1) % M  # 计算下一项
    fib0, fib1 = fib1, fib_next  # 更新前两项
    if fib0 == 0 and fib1 == 1:
        print(n)  
        break