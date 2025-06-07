# [蓝桥杯 2024 国 Python A] 设置密码
T = int(input())

# 定义合法特殊字符集合
special_chars_set = set('~!@#$%^&*()_')

for _ in range(T):
    s = input()
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_types_count = 0
    
    # 用于记录已遇到的特殊字符，防止重复计数种类
    seen_special_chars = set() 

    # 检查合法性并统计字符类型
    is_valid_char = True
    for char in s:
        if 'A' <= char <= 'Z':
            has_upper = True
        elif 'a' <= char <= 'z':
            has_lower = True
        elif '0' <= char <= '9':
            has_digit = True
        elif char in special_chars_set:
            has_special = True
            if char not in seen_special_chars:
                seen_special_chars.add(char)
                special_types_count += 1
        else:
            is_valid_char = False
            break
    
    # 如果包含不合法字符，直接输出0
    if not is_valid_char:
        print(0)
        continue
        
    n = len(s)
    
    # 统计包含的字符类型数量
    char_type_count = 0
    if has_upper:
        char_type_count += 1
    if has_lower:
        char_type_count += 1
    if has_digit:
        char_type_count += 1
    if has_special:
        char_type_count += 1
        
    # 强密码判断
    is_strong = False
    if n >= 12:
        if char_type_count == 4: # 同时包含四种
            is_strong = True
        # 包含特殊字符在内的其中三种，且特殊字符种类数 >= 3
        if char_type_count >= 3 and has_special and special_types_count >= 3:
            is_strong = True
    
    if is_strong:
        print(3)
        continue

    # 中密码判断
    is_medium = False
    if n >= 8 and char_type_count >= 2:
        is_medium = True
    
    if is_medium:
        print(2)
        continue
        
    # 弱密码判断
    is_weak = False
    if n >= 6:
        is_weak = True
        
    if is_weak:
        print(1)
        continue
        
    # 都不满足，则为不合法密码
    print(0)