n = input()
difficulty = list(map(int, input().split()))
for i in range(len(difficulty)):
    if difficulty[i] == 0:
        n = 0
        continue
    elif difficulty[i] == 1:
        print("HARD")
        n = 1
        break
if n == 0:
    print("EASY")
