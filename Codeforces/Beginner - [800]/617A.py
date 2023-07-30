x = int(input())
count = (x - x%5)/5
if x % 5 != 0:
    count += 1
print(int(count))
