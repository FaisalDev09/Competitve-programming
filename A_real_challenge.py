import math 

area = int(input())
side = math.sqrt(area)
perimeter = side * 4

if perimeter % 1 == 0:
    print(int(perimeter))
else:
    print(float(perimeter))



    
    
