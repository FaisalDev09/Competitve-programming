count = 0 # Outside the loop so that it does not reset to 0


while True:
    try:
        n, *sample = map(int, input().split())
        sample = sample[:n] # The list only adds number n (from 0-n)
        count += 1
        minimum  = min(sample)
        maximum = max(sample)
        range_val = maximum - minimum
        print(f"Case {count}: {minimum} {maximum} {range_val}")        
    except EOFError: 
        break
    except ValueError:
        break
