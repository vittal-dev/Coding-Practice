n = int(input())
i = 1
t = 0
while i <= n:
    problem = str(input())
    if problem.count("1") >= 2:
        t += 1
    i += 1
print(t)
