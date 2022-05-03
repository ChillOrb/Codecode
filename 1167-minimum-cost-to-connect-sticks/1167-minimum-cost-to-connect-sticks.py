class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        heapq.heapify(sticks)
        
        s=0
        while len(sticks) >1:
            total=heapq.heappop(sticks)+heapq.heappop(sticks)
            s+=total
            heapq.heappush(sticks,total)
            
        return s
            
        