n, k = map(int, input().split())

scores = list(map(int, input().split()))

count = 0
target = scores[k-1]

for score in scores:
    if score >= target and score > 0:
        count += 1

print(count)
