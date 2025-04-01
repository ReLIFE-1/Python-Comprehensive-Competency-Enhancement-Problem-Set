n = int(input())
m = int(input())

# 创建一个列表，包含1到n的数字
numbers = list(range(1, n + 1))

# 定义一个函数来计算一个数的数位和
def digit_sum(num):
    s = 0
    while num > 0:
        s += num % 10
        num = num // 10
    return s

# 根据数位和和数值本身进行排序
sorted_numbers = sorted(numbers, key=lambda x: (digit_sum(x), x))

# 输出第m个元素
print(sorted_numbers[m - 1])