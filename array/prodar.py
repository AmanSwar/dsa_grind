def productExceptSelf(nums):
    prefix_arr = [0] * len(nums)
    suffix_arr = [0] * len(nums)

    prefix_arr[0] = 1
    suffix_arr[-1] = 1

    for i in range(len(nums)):
        prefix_arr[i] = prefix_arr[i-1] * nums[i-1]
        
    for i in range(len(nums)-2 , 0 , -1):
        suffix_arr[i] = suffix_arr[i + 1] * nums[i + 1]
      
    ans = [0] * len(nums)

    for i in range(len(nums)):
        ans[i] = prefix_arr[i] * suffix_arr[i]

    return ans


nums = [0 ,0]

print(productExceptSelf(nums))
