class Solution:
    def frequencySort(self, s: str) -> str:
        s=list(s)
        s.sort()
    
        final=[]
        curr_sub=[]
        curr_sub.append(s[0])
        for char in s[1:]:
            if char !=curr_sub[-1]:
                
                final.append("".join(curr_sub))
                curr_sub=[]
                
                
            curr_sub.append(char)
            
        final.append("".join(curr_sub))
        
        
        final.sort(key=lambda s:len(s),reverse=True)
        
        return "".join(final)
            
            
            
        
        
            
        