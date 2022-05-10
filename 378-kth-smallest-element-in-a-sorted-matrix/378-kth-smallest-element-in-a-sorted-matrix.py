class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        
        heap=[]
        
        for row in range(0,len(matrix)):
            heapq.heappush(heap,(matrix[row][0],row,0))
            
            
        
        for i in range(k):
            ans,row,col=heapq.heappop(heap)

            if col+1<len(matrix[0]):
                heapq.heappush(heap,(matrix[row][col+1],row,col+1))
                
        return ans