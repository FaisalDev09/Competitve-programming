nums = list(map(int, input()))
n = len(nums)

# Step 1: Find the pivot
# S tart from the second last element, the last element is at i+1
i = n - 2
while i >= 0 and nums[i] >= nums[i+1]:
    i -= 1  # Move one step to the left

if i < 0:
    # If no pivot found, the list is in descending order
    # This means we are at the last permutation
    print(0)  # Optional: print 0 to indicate there was no next permutation
else:
    # Step 2: Find the smallest element in the suffix that is larger than the pivot
    j = len(nums) - 1  # Start from the last element
    while nums[j] <= nums[i]:
        j -= 1  # Move left until we find a number bigger than pivot

    # Step 3: Swap pivot with that element
    nums[i], nums[j] = nums[j], nums[i]

    # Step 4: Reverse the suffix (elements to the right of pivot)
    nums[i+1:] = reversed(nums[i+1:])

    print(*nums, sep="")
