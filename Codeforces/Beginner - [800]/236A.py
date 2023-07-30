input = input()
unique = ""
for i in range(len(input)):
    if input[i] in unique:
        continue
    else:
        unique = unique + input[i]
if len(unique)%2 == 0:
    print("CHAT WITH HER!")
elif len(unique)%2 == 1:
    print("IGNORE HIM!")
