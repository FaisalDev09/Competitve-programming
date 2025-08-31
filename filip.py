num_1, num_2 = input().split()

# reverse the number
num_1 = num_1[::-1] 
num_2 = num_2[::-1] 

# convert to int in order to compare
if int(num_1) > int(num_2):
    print(num_1)
else:
    print(num_2)