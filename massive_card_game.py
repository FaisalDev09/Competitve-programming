# Read the number of cards
n = int(input())  

# Read the list of cards
cards = list(map(int, input().split()))  

# Read the number of queries
q = int(input())  

# Process each query
i = 0
while i < q:
    l, r = map(int, input().split())  # Read the interval [l, r]
    i += 1
    total = 0 # Reset total for each query

    # Count how many times each number in [l, r] appears in cards
    for num in range(l, r + 1):
        total += cards.count(num)# Count occurrences of num

    print(total)   # Print result for this query





