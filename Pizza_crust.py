import math
r,c = map(int,input().split())

circle_area = (r*r) * math.pi
radius = r-c
cheese_area = radius * radius * math.pi

percent = float(cheese_area/circle_area)
print(percent*100)


