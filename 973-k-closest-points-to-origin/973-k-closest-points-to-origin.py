class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap=[]
        out=[]
        for point in points:
            d=0
            d+=point[0]**2+point[1]**2
            
            heapq.heappush(heap,(d,point))
                           
        for i in range(k):
            x=heapq.heappop(heap)
            out.append(x[1])
            
        return out 
            
            
            
            
        