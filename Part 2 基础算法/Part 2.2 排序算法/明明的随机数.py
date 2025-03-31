n = int(input())
nums = list(map(int,input().split()))
print(len(set(nums)))
print(*sorted(set(nums)))