s = input().strip()
lt = list(s.replace('-', ''))

sum = 0
for i in range(9):
    sum += int(lt[i]) * (i + 1)

mod = sum % 11

# 确定输入的识别码是什么
if lt[9] == 'X':
    actual_check_digit = 10
else:
    actual_check_digit = int(lt[9])

# 检查识别码是否与计算结果匹配
if mod == actual_check_digit:
    print("Right")
else:
    if mod == 10:
        correct_check_digit = 'X'
    else:
        correct_check_digit = str(mod)
    
    print(f"{s[:-1]}{correct_check_digit}")
