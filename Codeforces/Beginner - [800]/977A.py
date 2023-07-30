input = list(map(int, input().split()))
n = input[0]
k = input[1]

for i in range(k):
    if n%10 == 0:
        n = int(n/10)
    else:
        n = n-1

print(n)
