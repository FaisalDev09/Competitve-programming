n = int(input())
pivot_listan =  list(map(int, input().split()))

count = 0
left_array = [0] * n
right_array = [0] * n

left_array[0] = pivot_listan[0]
right_array[-1] = pivot_listan[-1]

for i in range(1,n):
    left_array[i] = max(left_array[i-1],pivot_listan[i])

for i in reversed(range(n-1)):
    right_array[i] = min(right_array[i+1], pivot_listan[i])


for i in range(n):
    if left_array[i] == right_array[i]:
        count += 1

print(count)

