def characterReplacement(s , k):

  left = 0
  right = 0

  char_set = set()
  hash_map = {}
  while(True):
    char_set.add(s[right])

    hash_map[s[right]] = hash_map.get(s[right] , 0) + 1
    


    
