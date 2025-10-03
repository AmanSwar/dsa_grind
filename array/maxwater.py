def maxArea(height):

  left  = 0
  right = len(height) - 1

  max_prod = 1

  while(left <= right):

    if(height[left] > height[right]):
      curr_prod = height[right] * (right-left)
      right -= 1
    else:
      curr_prod = height[left] * (right - left)
      left += 1

    if curr_prod > max_prod:
      max_prod = curr_prod

  return max_prod


height = [1,8,6,2,5,4,8,3,7]

print(maxArea(height))
    

      


