import math

pi = math.pi

while True:
    try:
        line  = input()
        if not line:
            break   
        r,x,y = map(float, line.split())    
    except EOFError:
        break

    distance = math.hypot(x,y)

    if distance > r:
        print("miss")
    else:
        h = r - distance 
        ratio = (r-h) / r
        base  = r - h
        inside_sqrt = 2 * r * h - h * h
        circle = pi * r*r

        smaller_part =  r * r * math.acos(ratio) - base * math.sqrt(inside_sqrt)
    
        larger_part = circle - smaller_part

        print(f"{larger_part:.7} {smaller_part:.7}")