class Node: 
    def __init__(self, d): 
        self.data = d 
        self.left = None
        self.right = None
  

# input : sorted array of integers 
# output: root node of balanced BST 
def sortedArrayToBST(arr): 
      
    if not arr: 
        return None
  
    # find middle 
    mid = (len(arr)) / 2
      
    # make the middle element the root 
    root = Node(arr[mid]) 
      
    # left subtree of root has all 
    # values <arr[mid] 
    root.left = sortedArrayToBST(arr[:mid]) 
      
    # right subtree of root has all  
    # values >arr[mid] 
    root.right = sortedArrayToBST(arr[mid+1:]) 
    return root 

def preOrder(node): 
    if not node: 
        return
      
    print node.data, 
    preOrder(node.left) 
    preOrder(node.right)  
  

#driver code
  
arr = [1, 2, 3, 4, 5, 6, 7] 
root = sortedArrayToBST(arr) 
print "PreOrder Traversal of constructed BST ", 
preOrder(root) 
