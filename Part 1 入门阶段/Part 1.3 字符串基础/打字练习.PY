# 处理退格键的函数
def process_backspaces(text):
    result = []
    for ch in text:
        if ch == '<':
            if result:
                result.pop()
        else:
            result.append(ch)
    return ''.join(result)

# 读取范文
original = []
while True:
    line = input()
    if line == 'EOF':
        break
    original.append(process_backspaces(line))

# 读取输入
input_text = []
while True:
    line = input()
    if line == 'EOF':
        break
    input_text.append(process_backspaces(line))

# 读取时间
T = int(input())

# 初始化总正确字符数
correct_count = 0

# 逐行比较
for i in range(min(len(original), len(input_text))):
    ori_line = original[i]
    inp_line = input_text[i]
    for j in range(min(len(ori_line), len(inp_line))):
        if ori_line[j] == inp_line[j]:
            correct_count += 1

# 计算KPM
kpm = int(round((correct_count / T) * 60))

# 输出结果
print(kpm)