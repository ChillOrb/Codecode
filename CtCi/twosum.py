def twoSum(nums, target):
    checker = {}
    for i, v in enumerate(nums):
        if target - v in checker:
            return [checker[target - v], i]
        else:
            checker[v] = i
    return []


print(twoSum([4, 2, 2, 7, 3], 5))
