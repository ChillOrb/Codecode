class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for count,val in enumerate(nums):
            remaining=target-val
            if remaining in seen:
                return [count,seen[remaining]]
            else:
                seen[val]=count
            
            