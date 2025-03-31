n, m = map(int, input().split())
candidates = []
for _ in range(n):
    candidates.append(list(map(int, input().split())))

candidates.sort(key=lambda x: (-x[1], x[0]))

threshold_index = min(int(m * 1.5), n) - 1
threshold_score = candidates[threshold_index][1]

qualified = [c for c in candidates if c[1] >= threshold_score]

print(threshold_score, len(qualified))
for k, s in qualified:
    print(k, s)