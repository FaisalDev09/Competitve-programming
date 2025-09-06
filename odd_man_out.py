n = int(input())
count = 0
while count < n:
    s = set()
    count += 1
    number = input()
    couple = list(map(int,input().split()))
    for i in couple:
        if i in s:
            s.remove(i)
        else:
            s.add(i)
    print(f"Case #{count}:",*s)

    

    
    

