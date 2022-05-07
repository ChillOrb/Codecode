from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        d1=Counter(tasks)


        heap=[]

        out=[]
        for key,val in d1.items():

            heapq.heappush(heap,(-val,key))

        time=0  


        while heap:
            i=0
            temp=[]
            while i<=n:
                time+=1
                if heap:
                    val,key=heapq.heappop(heap)
                    out.append(key)
                    if val!=-1:
                        temp.append((val+1,key))
                if not heap and not temp:
                    break
                else:
                    i+=1
            for item in temp:
                heapq.heappush(heap,item)

        return time