first_case = True

while True:
    n = int(input())
    if n == 0:
        break

    times = [input() for _ in range(n)]
    times_digital = []     # List to store tuples: ((hours, minutes in 24-hour format), original string)


    for t in times:
        original = t
        parts = t.split() # Split into time and "a.m./p.m."
        time_part = parts[0].split(":") # Split hours and minutes
        hours, minutes = int(time_part[0]), int(time_part[1])
        z = parts[1]# "a.m." or "p.m."
        
        # Convert to 24-hour format for correct sorting
        if z.lower() == "a.m.":
            if hours == 12: # 12 a.m. -> 0
                hours = 0
        elif z.lower() == "p.m.":
            if hours != 12:
                hours += 12 # 1-11 p.m. -> add 12
        
        # Append a tuple of (24-hour time, original string)
        times_digital.append(((hours, minutes), original))
    # Sort appointments based on 24-hour time
    sorted_times = sorted(times_digital, key=lambda x: x[0])
    
    # Print a blank line between test cases (except before the first)
    if not first_case:
        print()
    first_case = False
    
    # Print the original appointment strings in sorted order
    for _, original in sorted_times:
        print(original)
