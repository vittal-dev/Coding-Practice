n = int(input())
change = []
capacity = 0
min = 0
for i in range(n):
    change.append(list(map(int, input().split())))
    capacity -= change[i][0]
    capacity += change[i][1]
    if min < capacity:
        min = capacity
print(min)
