bear = list(map(int, input().split()))
count = 0
while bear[0] <= bear[1]:
    bear[0] *= 3
    bear[1] *= 2
    count += 1
print(count)
