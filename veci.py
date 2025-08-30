nums = list(map(int, input()))

if nums == sorted(nums, reverse=True):
    print("0")
else:
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i-= 1
    
    
