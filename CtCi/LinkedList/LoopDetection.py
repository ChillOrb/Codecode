# using hashing 

# Python program to detect loop 
# in the linked list 

# Node class 
class Node: 

	# Constructor to initialize 
	# the node object 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 

	# Function to initialize head 
	def __init__(self): 
		self.head = None

	# Function to insert a new 
	# node at the beginning 
	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	# Utility function to print it 
	# the linked LinkedList 
	def printList(self): 
		temp = self.head 
		while(temp): 
			print (temp.data, end =" ") 
			temp = temp.next


	def detectLoop(self): 
		s = set() 
		temp = self.head 
		while (temp): 
		
			# If we have already has 
			# this node in hashmap it 
			# means their is a cycle 
			# (Because you we encountering 
			# the node second time). 
			if (temp in s): 
				return True
	
			# If we are seeing the node for 
			# the first time, insert it in hash 
			s.add(temp) 
	
			temp = temp.next
		
	
		return False

# Driver program for testing 
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(10) 

# Create a loop for testing 
llist.head.next.next.next.next = llist.head; 

if( llist.detectLoop()): 
	print ("Loop found") 
else : 
	print ("No Loop ") 

# using Floyd loop detect of fast , slow runner  

# Python program to detect loop in the linked list 

# Node class 
class Node: 

	# Constructor to initialize the node object 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 

	# Function to initialize head 
	def __init__(self): 
		self.head = None

	# Function to insert a new node at the beginning 
	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	# Utility function to print it the linked LinkedList 
	def printList(self): 
		temp = self.head 
		while(temp): 
			print temp.data, 
			temp = temp.next


	def detectLoop(self): 
		slow_p = self.head 
		fast_p = self.head 
		while(slow_p and fast_p and fast_p.next): 
			slow_p = slow_p.next
			fast_p = fast_p.next.next
			if slow_p == fast_p: 
				return

# Driver program for testing 
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(10) 

# Create a loop for testing 
llist.head.next.next.next.next = llist.head 
if(llist.detectLoop()): 
		print "Found Loop"
else: 
		print "No Loop"

