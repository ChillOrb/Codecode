class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(0,len(image)):
            image[i]=image[i][::-1]
            for j in range(0,len(image[0])):
                image[i][j]=image[i][j]^1
                
                
        return image