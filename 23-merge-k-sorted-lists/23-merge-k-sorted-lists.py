# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        combined=[]
        for i in lists:
            while i:
                combined.append(i.val)
                i=i.next
                
        combined=sorted(combined)
        print(combined)
        
        dummy=node=ListNode(0,None)
        for i in range(0,len(combined)):
            node.next=ListNode(combined[i])
            node=node.next
            
        return dummy.next
            
            
        