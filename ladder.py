import math

height, angle = map(int, input().split())

# Convert angle from deegres to radians(python math functions use radians)
radians = math.radians(angle)

# Calculate the minimum ladder length needed
sin_value = math.sin(radians)

# Calculate the minimum ladder length needed
ladder = height / sin_value
# Round up to the nearest whole number 
ladder_ceil = math.ceil(ladder)

print(ladder_ceil)
