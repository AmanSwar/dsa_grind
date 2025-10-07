def subsets(nums):
  lenArray = len(nums)
  final_arry = []
  empty_arr = []
  def f(curr_index , curr_arr):

    nonlocal final_arry
    
    if curr_index == lenArray:
      final_arry.append(curr_arr)
      return
    
    f(curr_index+1 , curr_arr + [nums[curr_index]])
    f(curr_index + 1 , curr_arr)

  f(0 , empty_arr)
  return final_arry


nums = [1,2,3]
print(subsets(nums))