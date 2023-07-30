b = input().split()
n = int(b[0])
k = int(b[1])
a = input().split()
i = 0
adv = 0
while i < n:
    if int(a[i]) > 0 and int(a[i]) >= int(a[k-1]):
        adv += 1
    i += 1
print(adv)
