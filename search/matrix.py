def searchMatrix(matrix , target):
  
  for sub in range(len(matrix)):

    if matrix[sub][0] == target: return True

    if matrix[sub][0] > target:
        print(matrix[sub])
        if target in matrix[sub]: return True

  return False
        


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,40]] 
target = 3

print(searchMatrix(matrix , target))