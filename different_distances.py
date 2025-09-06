import math 

line = input()
result = 0.0
while line != "0":
    x1, y1, x2, y2, p = map(float,line.split())
    if p == 2:
        result = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    elif p==1:
        result = abs(x1 - x2) + abs(y1-y2)
    else:
        result = (abs(x1 - x2) ** p + abs(y1 - y2)**p) ** (1/p)
    print(result)
    line = input()



