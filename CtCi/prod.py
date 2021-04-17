def RecurProd(nums):
    nums2 = []

    def product(nums):

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            prod = 1
            for i in nums:
                prod = prod*i

            return prod
    for i in range(0, len(nums)):
        if i == 0:
            nums2.append(product(nums[0:i+1])*product(nums[i+1:]))
        elif i == len(nums)-1:
            nums2.append(product(nums[0:i]))
        else:
            nums2.append(product(nums[0:i])*product(nums[i+1:]))

    return nums2


print(RecurProd([]))
