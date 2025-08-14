# Read the numbers of elements
n = int(input()) # example: 8
# Read the array of integers
a = list(map(int, input().split())) # example: 2 1 3 4 7 5 6 8


# Create prefix max (left) and suffix min (right) arrays
left = [0] * n
right = [0] * n

# Set the first element for left (prefix max) and last element for right (suffix min) 
left[0] = a[0]
right[-1] = a[-1]

# Build prefix min array. left[i] = max of all elements from start to i 
for i in range(1,n):
    left[i] = max(left[i-1],a[i])

#Build suffix max array. right[i] = min of all elements i to end
for i in reversed(range(n-1)):
    right[i] = min(right[i+1], a[i])

# Possible pivot position 
count = 0
for i in range(n):
    if left[i] == right[i]:
        count += 1
print(count) # Output for example input above: 3
