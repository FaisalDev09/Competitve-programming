n = int(input())
a = list(map(int, input().split()))

left = [0] * n
right = [0] * n

left[0] = a[0]
right[-1] = a[-1]

for i in range(1,n):
    left[i] = max(left[i-1],a[i])

for i in reversed(range(n-1)):
    right[i] = min(right[i+1], a[i])

count = 0
for i in range(n):
    if left[i] == right[i]:
        count += 1
print(count)