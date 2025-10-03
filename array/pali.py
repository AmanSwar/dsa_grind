def isPalindrome(s : str):

  

  new_stirng = ""

  for i in s:
    if i.isalnum():
      new_stirng += i.lower()
  left = 0
  right = len(new_stirng)-1
  while(left <= right):

    if(new_stirng[left] != new_stirng[right]):
      return False
    
    left += 1
    right -= 1

  return True


s = "race a car"

print(isPalindrome(s))
