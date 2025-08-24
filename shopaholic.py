n = int(input()) 
costs = list(map(int, input().split()))
costs.sort(reverse = True ) # Sorting from largest to smallest value 

count = 0 # Count variable to calculate total discount 
for i in range(2,len(costs), 3) : # start at index 2 (element 3), ends at the end of the list and  a step size =  3 
    count += costs[i]

print(count)