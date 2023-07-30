# k,n,w
# k - cost of 1st banana, n - money in pocket, w - bananas to buy
total = 0
borrow = 0
b = list(map(int, input().split()))
for i in range(b[2]):
    total += (i+1)*b[0]

if total <= b[1]:
    pass
elif total > b[1]:
    borrow = total - b[1]

print(borrow)
