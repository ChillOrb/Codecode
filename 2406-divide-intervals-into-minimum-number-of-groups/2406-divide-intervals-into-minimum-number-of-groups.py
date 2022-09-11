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