n = int(input())
x = 0

while x < n:
    x += 1 
    str_1 = input()
    str_2 = input()
    
    index = len(str_1)
    result = [] 
    for j in range(index):
        if str_1[j] == str_2[j]:
            result.append(".")
        else:
            result.append("*")
    print(str_1)
    print(str_2)
    print(*result,sep="")
    print()

