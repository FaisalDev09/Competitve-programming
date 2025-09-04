num = list(map(int, input()))
n = len(num)
i = n-2

while num[i] > 0 and num[i] >= num[i+1]:
    i -=1

if i < 0:
    print(0)
else:
    j = n-1
    while num[j] <= num[i]:
        j -= 1
    
    num[i],num[j] = num[j], num[i]

    num[i+1:] = sorted(num[i+1:])

    print(*num,sep="")

