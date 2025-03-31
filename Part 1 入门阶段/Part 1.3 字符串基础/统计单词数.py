supstr = input().lower() 
string = input().lower() 

supstr_list = string.split(" ") 
count = 0 # 出现的次数
first_pos = -1 # 第一次出现的位置
length = 0 # 用于计算第一次出现位置的累加长度

for i, w in enumerate(supstr_list): 
  # 统计待查找字符串出现的个数
  if w == supstr: 
    count += 1
    # 如果是第一次出现，计算位置
    if first_pos == -1:
        for j in range(i):
            length += len(supstr_list[j]) + 1
        first_pos = length

if count > 0:
  print(count, first_pos)
else:
  print(-1)