def twosum (nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return hashmap[complement],i 
        hashmap[nums[i]] = i
result = twosum([10,20,30,40], 30)
print (result)
















# def twosum (nums, target):
#     for i in range(len(nums)):# first iteration i = 0 and nums[i] = 3
#         # print(i, nums[i])
#         for j in range(i + 1, len(nums)):
#             if nums[j] == target - nums[i]:
#                 return [i,j]
#     print("No solution found")

# result = twosum([3,4,5,],8)
# print (result)




    


