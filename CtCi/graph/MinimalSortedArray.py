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
