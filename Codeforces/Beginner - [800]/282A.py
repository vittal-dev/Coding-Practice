n = int(input())
x = 0
for i in range(n):
    r = input()
    if "++" in r:
        x += 1
    if "--" in r:
        x -= 1
print(x)
