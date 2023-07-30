a = []
for i in range(2):
    a.append([*map(str, input().split())])

for i in range(len(a[0])):
    if a[0][i].lower() == a[1][i].lower():
        print(0)
    elif a[0][i].lower() >= a[1][i].lower():
        print(1)
    elif a[0][i].lower() <= a[1][i].lower():
        print(-1)

# ord() function turns unicode string into its integer unicode point value