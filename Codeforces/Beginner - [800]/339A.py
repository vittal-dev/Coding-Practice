string = str(input())
output = ""
for i in range(string.count("1")):
    output += "1+"
for i in range(string.count("2")):
    output += "2+"
for i in range(string.count("3")):
    output += "3+"
output = output[:-1]
print(output)
