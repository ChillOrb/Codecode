class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        if n==0:
            return 1
        
        
        l=floor(log2(n))+1
        
        
        bitmask=(1<<l)-1
        
        
        return bitmask^n