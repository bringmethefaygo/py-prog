class Node:
	def __init__(self,key):
		self.left = None 
		self.right = None 
		self.data = key

def printlevelorder(root):
	h = height(root)
	for i in range(1,h+1):
		printcurrent(root,i)

def printcurrent(root,level):
	if root is None:
		return
	if level==1:
		print(root.data,end=" ")
	elif level>1:
		printcurrent(root.left,level-1)
		printcurrent(root.right,level-1)

def height(root):
	if(root is None):
		return 0

	else:
		lheight = height(root.left)
		rheight=height(root.right)

		if(lheight>rheight):
			return lheight+1
		else:
			return rheight+1

root=Node(8)
root.left = Node(3)
root.right=Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right = Node(14)
root.right.right.left = Node(13)

printlevelorder(root)
print()

