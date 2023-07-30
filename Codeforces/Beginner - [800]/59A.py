s = input()
upper = 0
lower = 0
for i in range(len(s)):
    if s[i].isupper() == True:
        upper += 1
    else:
        lower += 1

if upper > lower:
    s = s.upper()
else:
    s = s.lower()
print(s)
