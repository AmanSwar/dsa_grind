from collections import defaultdict
def checkInclusion(s1 , s2):

            
    len_s1 = len(s1)

    left = 0
    right = len_s1

    hash_map_s1 = defaultdict(int)

    for s in s1:
        hash_map_s1[s] += 1
    while(right <= len(s2)):

        temp_hash_map = defaultdict(int) 

        for s in s2[left : right]:
            temp_hash_map[s] += 1

        left += 1
        right += 1

        if(hash_map_s1 == temp_hash_map):
            return True

    return False


s1 = "adc"
s2 = "dcda"
# s1 = "ab"
# s2 = "eidbaooo"
print(checkInclusion(s1 , s2))
