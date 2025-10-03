def topKFrequent(nums, k):

  hash_map = {}

  for n in nums: # N
    if hash_map.get(n):
      hash_map[n] += 1
    else:
      hash_map[n] = 1

  final_ans = []
  hash_map = sorted(hash_map.items() , key=lambda x : x[1] , reverse=True) # aloga (a = number of unqiue elements)
  for i in range(k):
    final_ans.append(hash_map[i][0])

  return final_ans

if __name__ == "__main__":
  arr = [3,3,2,3,2,2,2,1,1,1,1,1]
  k = 2
  topKFrequent(arr , k)



