
n, m = map(int,input().split())

sekvens = []
gnomes = set(range(1,n+1))
for _ in range(m):
    num = int(input())
    sekvens.append(num)

missing = sorted(gnomes - set(sekvens))

for i in sekvens: 
    




    

