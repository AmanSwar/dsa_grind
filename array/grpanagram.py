def groupAnagrams(strs :  list[str]):

  hash_map = {}

  for word in strs:

    letters = sorted(word)
    letter_string = "".join(letters)
    if hash_map.get(letter_string):
      hash_map[letter_string] += [word]
    else:
      hash_map[letter_string] = [word]
  
  final_ans = []
  for keys in hash_map:
    final_ans.append(hash_map[keys])

  return final_ans



if __name__ == "__main__":
  a = ["eat","tea","tan","ate","nat","bat"]

  groupAnagrams(a)