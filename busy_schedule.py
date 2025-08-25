all_times = []

while True:
    n = int(input().strip())
    if n == 0:
        break

    times = []
    for _ in range(n):
        times.append(input().strip())

    all_times.append(times)

print(all_times)




