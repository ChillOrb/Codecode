# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(l1,l2):
                dummy = node = ListNode()
                if l1==None and l2==None:
                    
                    return None
                if l1 is None:
                    node=l2
                    return node
                elif l2 is None:

                    node=l1
                    return node        
                while l1 and l2:

                    if l1.val == l2.val:
                        node.next=l1
                        node=node.next
                        l1=l1.next
                    elif l1.val<l2.val:
                        node.next=l1
                        node=node.next
                        l1=l1.next
                    else:
                        node.next=l2
                        node=node.next
                        l2=l2.next

                if l1==None:
                    node.next=l2
                else:
                    node.next=l1

                return dummy.next


        if len(lists)==0:
            return None
        combined=lists[0]
        for i in range(1,len(lists)):
            combined=mergeTwoLists(combined,lists[i])
        return combined

        
       