n = input()
count = n.count("4") + n.count("7")
string = str(count)
check = 1
for i in range(len(string)):
    if string[i] == "4":
        continue
    if string[i] == "7":
        continue
    else:
        check = 0
        print("NO")
        break
if check == 1:
    print("YES")