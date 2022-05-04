from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        ctr=Counter(nums)
        print(ctr)
        
        
        heap=[]
        
        for key,val in ctr.items():
            
            heapq.heappush(heap,(val,key))
           
        print(heap)
        for i in range(0,len(heap)-k):
            heapq.heappop(heap)
            
        return [y for x,y in heap]
        