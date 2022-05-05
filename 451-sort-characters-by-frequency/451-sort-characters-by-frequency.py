from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        
        d=Counter(s)
        count=[]
        for key,val in d.items():
            times=val
            while times!=0:
                count.append((val,key))
                times-=1
        
        print(count)
        
        heap=[]
        
        out=[]
        for key,val in count:
            heapq.heappush(heap,(key,val))
            
        print(heap)
            
        for i in range(0,len(heap)):
            out.append(heapq.heappop(heap)[1])
        print(out)
        return "".join(out[::-1])
            
        
        
        
        