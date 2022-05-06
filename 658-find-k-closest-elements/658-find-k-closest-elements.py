class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        
        
        for i in range (0,len(arr)):
            
            heapq.heappush(heap,(abs(x-arr[i]),arr[i]))
            
          
        print(heap)        
        final=[]        
        while k>0:
            final.append(heapq.heappop(heap)[1])
            k-=1
        
        
        return sorted(final)
            
                
                
            
        