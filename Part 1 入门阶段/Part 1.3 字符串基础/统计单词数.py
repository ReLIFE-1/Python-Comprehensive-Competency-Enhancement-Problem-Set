word = input().strip().lower()
words = input().strip().lower().split()
cnt = 0 
index = -1
cur = 0
for i in range(len(words)):
    cur = len(words[i]) + 1
    if words[i] == word:
        cnt += 1
        if index == -1:
            index = cur


if cnt == 0:
    print("-1")
else:
    print(f"{cnt} {index}")