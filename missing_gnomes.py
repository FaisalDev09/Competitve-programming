
n, m = map(int,input().split()) # n - total number of gnomes , m - number of gnomes which is left 

sekvens = [] # contains the left gnomes
gnomes = set(range(1,n+1))# all gnome numbers from 1 to n 
for _ in range(m):
    num = int(input())
    sekvens.append(num)

missing = sorted(gnomes - set(sekvens)) # contain the missing gnomes: all gnomes  - remaining gnomes, sorted in increasing order

result = [] # final result 
j = 0 # index för missing (to not use two loop)
i = 0 # index för sekvens

for _ in range(n): # The total number of gnomes is n 
    # Decide whetehr to take the next gnome from sekvens or missing
    if i <m and (j >= len(missing) or sekvens[i] < missing[j]):
        result.append(sekvens[i])
        i +=1
    else:
        result.append(missing[j])
        j +=1

for g in result:
    print(g)




    




    

