
#O(N) time and O(1) space best solution 


def isPalindrome(self, head):
    # rev records the first half, need to set the same structure as fast, slow, hence later we have rev.next
    rev = None
    # initially slow and fast are the same, starting from head
    slow = fast = head
    while fast and fast.next:
        # fast traverses faster and moves to the end of the list if the length is odd
        fast = fast.next.next
        
        # take it as a tuple being assigned (rev, rev.next, slow) = (slow, rev, slow.next), hence the re-assignment of slow would not affect rev (rev = slow)
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
       # fast is at the end, move slow one step further for comparison(cross middle one)
        slow = slow.next
    # compare the reversed first half with the second half
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    
    # if equivalent then rev become None, return True; otherwise return False 
    return not rev
























def is_palindrome(self):
        # Method 1:
        # s = ""
        # p = self.head 
        # while p:
        #     s += p.data
        #     p = p.next
        # return s == s[::-1]

        # Method 2:
        # p = self.head 
        # s = []
        # while p:
        #     s.append(p.data)
        #     p = p.next
        # p = self.head
        # while p:
        #     data = s.pop()
        #     if p.data != data:
        #         return False
        #     p = p.next
        # return True

        # Method 3
        p = self.head 
        q = self.head 
        prev = []
        
        i = 0
        while q:
            prev.append(q)
            q = q.next
            i += 1
        q = prev[i-1]
    
        count = 1

        while count <= i//2 + 1:
            if prev[-count].data != p.data:  # - count is first -1 means the last element , then -2 which means the second last element 
                return False
            p = p.next
            count += 1
        return True

# Example palindromes:
# RACECAR, RADAR

# Example non-palindromes:
# TEST, ABC, HELLO

llist = LinkedList()
llist.append("R")
llist.append("A")
llist.append("D")
llist.append("A")
llist.append("R")

llist_2 = LinkedList()
llist_2.append("A")
llist_2.append("B")
llist_2.append("C")

print(llist.is_palindrome())
print(llist_2.is_palindrome())
