t = int(input())
output = []
for i in range(t):
    def num_good(n = int(input()), arr = list(map(int, input().split()))):
        count = 0
        sum = 0
        for i in range(n):
            sum += arr[i]
        if sum < 0:
            count += (abs(sum) + abs(sum)%2)/2
            if (arr.count(-1) - count)%2 == 1:
                count += 1
        else:
            if arr.count(-1)%2 == 1:
                count += 1
        output.append(count)
    num_good()
for i in range(t):
    print(int(output[i]))