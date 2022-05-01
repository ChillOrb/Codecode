class Solution:
    def numTrees(self, n: int) -> int:
        
        def countrees(n,cache):
            
            
            if n==1:
                return 1
            if n==0:
                return 1
            
            if cache.get(n, -1) != -1: # -1 means we don't know countTrees(n) yet.
                return cache[n]
            
            result=0
            for i in range(1,n+1):
                
                left=countrees(i-1,cache)
                right=countrees(n-i,cache)
                
                
                result+=left*right
                
                
                cache[n]=result
                
                
            return result
        
        cache={0:1,1:1}
        countrees(n,cache)
        return cache[n]
            
            
        