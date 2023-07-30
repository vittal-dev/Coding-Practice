n = int(input())
input = list(map(int, input().split()))
output = []
for i in range(n):
    output.append(0)
    output[i] = input.index(i+1) + 1
    print(output[i], end = " ")