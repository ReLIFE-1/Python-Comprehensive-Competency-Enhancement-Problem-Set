L, N, M = map(int, input().split())
rocks = [int(input()) for _ in range(N)]
rocks.sort()

rocks.append(L)

left, right = 1, L
result = 0

while left <= right:
    mid = (left + right) // 2
    removed = 0
    prev = 0
    for rock in rocks:
        if rock - prev < mid:
            removed += 1
            if removed > M:
                break
        else:
            prev = rock
    if removed <= M:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)