class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        groups = []
        print(intervals)
        
        for interval in intervals:
            start, end = interval
            if groups and groups[0] < start: # if start of new interval is > minimum end , that means they are NOT intersecting and only one of them should be in heap so remove one 
                heappop(groups)
            heappush(groups, end)
            
        return len(groups)
    
    
    
    """
    class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        maxrooms=float('-inf')
        
        rooms=0
        
        merged=[]
        
        for i in range(0,len(intervals)):
            
            merged.append((intervals[i][0],1))
            merged.append((intervals[i][1]+1,-1))
            
            
        merged.sort()
        
        print(merged)
        
        
        for i in range(0,len(merged)):
            rooms+=merged[i][1]
            maxrooms=max(rooms,maxrooms)
            
        return maxrooms
        return len(allgroup)
                """