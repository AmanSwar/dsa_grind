def twoSum(nums, target):

    all_nums = {}
    for n in range(len(nums)):
      all_nums[nums[n]] = n

    for n in range(len(nums)):
       counter = abs(target - nums[n])
       if all_nums[counter]:
          return [n , all_nums[counter]]
    


arr = [2, 7, 11, 15]
keys = 9

print(twoSum(arr , keys))
