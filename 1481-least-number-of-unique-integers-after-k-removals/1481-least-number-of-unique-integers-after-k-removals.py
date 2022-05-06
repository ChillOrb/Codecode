from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        d=Counter(arr)
        print(d)
        heap=[]
        for key,val in d.items():
            for i in range(val):
                heapq.heappush(heap,(val,key))
                
                
            
        print(heap)
        while k>0:
            heapq.heappop(heap)
            k-=1
            
            
        return len(set(heap))