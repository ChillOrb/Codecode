# this creates new list and adds bigger to tail and smaller to head

# (using the existing nodes)  
# and return head of new list. 
def partition(head, x): 
      
    
    
    # Let us initialize start and 
    # tail nodes of new list  
    tail = head 
  
    # Now iterate original list  
    # and connect nodes 
    curr = head 
    while (curr != None): 
        next = curr.next
        if (curr.data < x): 
              
            # Insert node at head.  
            curr.next = head 
            head = curr 
          
        else: 
              
            # Append to the list of greater values 
            # Insert node at tail.  
            tail.next = curr 
            tail = curr 
          
        curr = next
      
    tail.next = None
  
    # The head has changed, so we need 
    # to return it to the user. 
    return head 
  
# Function to print linked list  
def printList(head): 
    temp = head 
    while (temp != None): 
        print(temp.data, end = " ") 
        temp = temp.next
