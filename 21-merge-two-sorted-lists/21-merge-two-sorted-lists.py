# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None or list2 is None:
            return list1 or list2
        
        
        start=dummy=ListNode(0,None)
        
        while list1 and list2:
            if list1.val<=list2.val:
                dummy.next=list1
                dummy=dummy.next  
                list1=list1.next
                
                
            elif list2.val<list1.val:
                dummy.next=list2
                dummy=dummy.next 
                list2=list2.next
                
            
        if list1 == None:
            dummy.next=list2
            
        else:
            dummy.next=list1
        
        return start.next