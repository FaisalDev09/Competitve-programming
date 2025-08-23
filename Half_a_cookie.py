import math
# Define pi 
pi = math.pi 

# Loop over all test cases until input ends
while True:
    try:
        line = input() # Read a line of input
        if not line:   # If the line is empty, break the loop
            break
        r, x, y = map(float, line.split()) # Split the line into three floats: radius, x and y
    except EOFError:   # Stop the loop if end-of-file is reached
        break
   
    # Calculate distance from the center (0,0) to the point (x,y)
    distance = math.hypot(x, y)
    
    # If the point is outside the circle, print("miss")
    if distance >= r:
        print("miss")
    else:
        # Calculate the height of the smaller circular segment
        h = r - distance
        
        # Formula for the area of the samller segment of the circle
        segment_a = r*r*math.acos((r-h)/r) - (r-h)*math.sqrt(2*r*h - h*h)
        
        # Total area of the circle 
        circle_a = pi * r*r

        # The larger piece is the rest of the circle 
        remaining_a = circle_a - segment_a
        
        # Print the two areas with the smaller on first, rounded to 7 decimal places
        if remaining_a < segment_a:
            print(f"{segment_a:.7f} {remaining_a:.7f}")
        else:
            print(f"{remaining_a:.7f} {segment_a:.7f}")
