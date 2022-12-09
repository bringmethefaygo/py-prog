
class Node:
	def __init__(self,key):
		self.right = None 
		self.left = None 
		self.val = key

	# inorder traversal
	def inorder(self):
		if(self.left):
			self.left.inorder()
		print(self.val,end =" ")
		if(self.right):
			self.right.inorder()


	# preorder traversal
	def preorder(self):
		print(self.val,end=" ")
		if(self.left):
			self.left.preorder()
		if(self.right):
			self.right.preorder()


	# postorder traversal
	def postorder(self):
		if(self.left):
			self.left.postorder()
		if(self.right):
			self.right.postorder()
		print(self.val,end=" ")


root = Node(1)
root.left = Node(2)
root.right=Node(3)
root.left.left = Node(10)
root.left.right = Node(12)


root.inorder()
print()

root.postorder()
print()

root.preorder()
print()

