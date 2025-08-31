name = input()
parts = name.split("-")
result = []
for i in parts:
    result.append(i[0])

print(*result, sep="")