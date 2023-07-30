n = int(input())
win = list(map(str, input().split()))
winCount_A = 0
winCount_D = 0
for i in range(len(win[0])):
    if win[0][i] == "A":
        winCount_A += 1
    elif win[0][i] == "D":
        winCount_D += 1
if winCount_A > winCount_D:
    print("Anton")
elif winCount_A < winCount_D:
    print("Danik")
else:
    print("Friendship")
