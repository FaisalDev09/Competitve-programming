nums = list(map(int,input()))
n = len(nums)
i = n - 2 
# Step 1: find the pivot
while i >= 0 and nums[i] >= nums[i+1]:
    i -= 1
# Step 2: If no pivot is found, the list is the largest permutation
# Return the first permutation by reversing the list
if i < 0:
    nums.reverse()
    print(nums)
# Step 3: If pivot exists, find the smallest number in the after the pivot that is larger than pivot
else:
    j = n - 1
    while nums[j] <= nums[i]:
        j -= 1
    # Step 4:  Switch place with the pivot and smallest largest number 
    nums[i], nums[j] = nums[j], nums[i]
    
    # Step 5: Sort the number after the pivot
    nums[i+1:] = sorted(nums[i+1:])
    
    # Step 6: Print the next permutation as a single number
    print(*nums, sep="")

