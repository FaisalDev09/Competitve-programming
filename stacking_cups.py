n = int(input())
cups = []

for x in range(n):
    a, b = input().split()

    if a.isalpha():        
        color = a
        radius = int(b)   
    else:
        radius = int(a) // 2
        color = b
    
    cups.append((radius, color))

cups.sort()

for r, color in cups:
    print(color)
