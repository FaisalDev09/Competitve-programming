import math # Start with improting math to use math functions

# ask for the number of test cases
num_test_cases = int(input())

# Loop over each test case
for _ in range(num_test_cases):
    # Read the the number of segments in this test case
    num_segments = int(input())
    
    # Robot starting position at the origin (0,0)
    x = 0
    y = 0
    angle = 90  # Start facing positive y-axis
   
    # Loop over each movement segment
    for _ in range(num_segments):
        rotation, distance = map(float, input().split())
        
        # Update the robot's current direction
        angle += rotation

        # convert the current angle to radians for math functions
        radians = math.radians(angle)

        # Update x and y coordinates based on the movement in this direction
        x += math.cos(radians) * distance
        y += math.sin(radians) * distance
    
    print(f"{x:.6f} {y:.6f}")




