
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        dummy=node=ListNode(0,None)
        for i in range(0,len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,i))

                
        # print(heap)        
        while heap:
            val,index=heapq.heappop(heap)
            # print(val,index)
            
            dummy.next=ListNode(val)
            
            dummy=dummy.next
            
            if lists[index].next:
                lists[index]=lists[index].next
                heapq.heappush(heap,(lists[index].val,index))
                print(heap)
                
                
        return node.next
        
        
        