n = int(input())
nums = input().split()

def compare(a, b):
    return int(b + a) - int(a + b)

from functools import cmp_to_key
nums.sort(key=cmp_to_key(compare))
print("".join(nums))