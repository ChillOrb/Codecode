class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        heap=[]
        
        for i in sticks:
            heapq.heappush(heap,i)
            
            
        s=0  
        total=0
        while len(heap) >1:
            total=heapq.heappop(heap)+heapq.heappop(heap)
            s+=total
            heapq.heappush(heap,total)
            
        return s
            
        