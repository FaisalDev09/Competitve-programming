while True:
    n = int(input())
    if n == 0:
        break
     
    my_dict = {} # Create a dictionary to store item and list of names
    for i in range(n):
        line = input().split()
        name = line[0]
        items = line[1:]

        for item in items: # Loop through items and add the customer to each item’s list
            if item not in my_dict:
                my_dict[item] = []
            if name not in my_dict:
                my_dict[item].append(name)

        
    for item, names in sorted(my_dict.items()): # Sort the items alphabetically
        print(item, *sorted(names)) # sort the names alphabetically
    print() # Blank line after each day's report


    
    





