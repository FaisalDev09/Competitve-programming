# Check if a list is sorted

v  = [1,2,5,3,4]
is_sorted = all(v[i] <= v[i+1] for i in range(len(v)-1))
print(is_sorted)


# How to sort a list
a = [1,4,5,3]
a.sort()
print(a)

# If you want top keep the orginal list
b = [1,9,6,8]
c = sorted(b)
print(b)
print(c)

# sort in descending order
d = [1,2,3,4,5]
d.sort(reverse = True)
print(d)

# Sort after absolute value
e = [3,-1, 1, -2, 2,]
e.sort(key=abs)
print(e)

# Sort only up to number x 
f = [2,24,5,2,1,35,]
f[:10] = sorted(v[0:3])
print(f)



