n = int(input())

vikter = list(map(int, input().split()))

if len(vikter) != n:
    print("fel")
    exit()
sorterade_vikter = sorted(vikter)
resultat = {}
for i , vikt in enumerate(sorterade_vikter): 
    resultat [vikt]  = i

for v in vikter:
    print(resultat[v], end=' ')
    











    
    
        
