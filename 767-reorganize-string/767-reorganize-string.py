from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        maxheap=[]
        
        
        d1=Counter(s)
        
        out=[]
        for key,val in d1.items():
            heapq.heappush(maxheap,(-val,key))
            
        print(maxheap)
        
        prev_val,prev_key=0,""
        while maxheap:
            
            
            val,key=heapq.heappop(maxheap)
            out.append(key)
            if prev_val<0:
                heapq.heappush(maxheap,(prev_val,prev_key))
                    
            val+=1
                
            prev_val,prev_key=val,key
            
        out="".join(out)
        if len(out)!=len(s):
            return ""
        
        return out
                
                

            
                
            
            
            
            
        
        
        
        