a = str(input().strip())
cnt = 0
for char in a:
    if char.isalnum():
        cnt += 1
print(cnt)