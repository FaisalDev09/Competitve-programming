
r, c, v, h = map(int, input().split()) # rov, column, vertically, horizontally 

x = 0 
while x < r: 
    x += 1
    char = input()
    result = [] 
    for i in char: #  multiply each character by value of h         
        result.append(i * h)
    for j in range(v): # 
        print(*result, sep="") # print the result v - times


