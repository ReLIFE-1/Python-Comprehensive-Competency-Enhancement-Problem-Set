''' [蓝桥杯 2023 省 Python B] 松散子序列 '''
s = input()
n = len(s)

def get_val(c):
  return ord(c) - ord('a') + 1  # ord()返回一个字符的 Unicode 编码值

# 处理边界情况
if n == 0:
  print(0)
elif n == 1:
  print(get_val(s[0]))
else:
  dp = [0] * n
  
  dp[0] = get_val(s[0])
  dp[1] = max(get_val(s[0]), get_val(s[1]))
  
  for i in range(2, n):
    val = get_val(s[i])
    dp[i] = max(dp[i-1], dp[i-2] + val)
  
  print(dp[n-1])