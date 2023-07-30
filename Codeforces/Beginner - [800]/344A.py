n = int(input())
magnet = ""
count = 0
for i in range(n):
    magnet += input()
for i in range(n-1):
    if magnet[(2*i)+1] == magnet[(2*i)+2]:
        count += 1
print(count + 1)