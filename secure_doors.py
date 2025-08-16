# number of log entries from input
n = int(input())

# Create a set to keep track of who is currently inside the building
inside = set()

for _ in range(n):
    action,name = input().split()
    
    # If the person is trying to enter
    if action == "entry":
        if name in inside:
            print(name, "entered (ANOMALY)")
        else:
            print(name, "entered")
            
            inside.add(name)
    # If the person is trying to exit
    elif action == "exit":
        if name not in inside:
            print(name,"exited (ANOMALY)")
        else:
            print(name,"exited")
            inside.discard(name)
    

