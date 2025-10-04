def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    low = 0
    high = len(nums)-1

    while low <= high:

        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            low = mid + 1
            continue
        else:
            high = mid - 1
            continue

    return -1


arr = [-1, 0, 3, 5, 9, 12]
num = 13

print(search(arr ,num))
