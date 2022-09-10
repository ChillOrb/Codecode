class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
            ans=[nums[0]]
            for i in range(1,len(nums)):
                if nums[i]>ans[-1]:
                    
                    ans.append(nums[i])
                    
                else:
                    j=0
                    
                    while nums[i]>ans[j]:
                        j+=1
                        
                    ans[j]=nums[i]
                        
                    
                        
                        
            return len(ans)
        