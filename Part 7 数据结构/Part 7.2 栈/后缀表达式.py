s = input().strip()
stack = []
i = 0
n = len(s)
while i < n:
    if s[i] == '@':
        break
    if s[i] == '.':
        i += 1
        continue
    if s[i] in '+-*/':
        b = stack.pop()
        a = stack.pop()
        if s[i] == '+':
            stack.append(a + b)
        elif s[i] == '-':
            stack.append(a - b)
        elif s[i] == '*':
            stack.append(a * b)
        elif s[i] == '/':
            # 向0取整处理
            if a * b < 0 and a % b != 0:
                stack.append(a // b + 1)
            else:
                stack.append(a // b)
        i += 1
    else:
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        stack.append(num)
print(stack[0])