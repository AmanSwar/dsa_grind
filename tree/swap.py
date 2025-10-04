from typing import List

def swap(node_index : int , arr : List) -> List:

    left_index = 2 * node_index + 1;
    right_index = 2 * node_index + 2;
    output_arr = []
    if(left_index < len(arr) and right_index < len(arr)):
        left_ele = arr[left_index]
        right_ele = arr[right_index]
        output_arr.append(right_ele)
        output_arr.append(left_ele)
        return output_arr
    
    return []

    


def soln(arr : List , N: int) -> List:

    for i in range(N):

        out = swap(i , arr)
        if out != []:
            arr[2*i + 1] = out[0]
            arr[2*i + 2] = out[1]
    return arr


array = [4,2,7,1,3,6,9]

print(soln(array , len(array))) 
print(soln(array , len(array)) == [4,7,2,9,6,3,1])
