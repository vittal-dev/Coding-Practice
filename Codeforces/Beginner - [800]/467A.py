n = int(input())
count = 0
for i in range(n):
    dorms = list(map(int, input().split()))
    if dorms[1] - dorms[0] >= 2:
        count += 1
print(count)
