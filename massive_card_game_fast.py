from bisect import bisect_left, bisect_right

n = int(input()) #  Number of cards
cards = sorted(map(int, input().split())) #  # Read the cards and sort them; sorted() returns a new sorted list
q = int(input()) #  Number of intervals (queries)



for i in range(q):  # Process each query (interval)
    l, r = map(int, input().split()) # Read the interval [l, r]
    left = bisect_left(cards, l)  # Index of the first card >= l
    right = bisect_right(cards, r)   # Index of the first card > r (just after the last r)
    total = right - left      # Number of cards within [l, r]
    print(total)         # Output the result for this query
