class Node:
	def __init__(self,data):
		self.next = None 
		self.data = data

class Linkedlist:
	def __init__(self):
		self.head = None 

	def addbegin(self,data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def addbetween(self,data,pos):
		new_node = Node(data)
		prev = self.head
		while(pos>2):
			prev = prev.next
			pos = pos-1

		new_node.next = prev.next
		prev.next = new_node


	def printlist(self):
		temp = self.head
		while(temp!=None):
			print(temp.data,end=" ")
			temp = temp.next
		print()

	def addend(self,data):
		new_node = Node(data)
		temp = self.head
		while(temp.next!=None):
			temp = temp.next
		temp.next = new_node

	def deletebeg(self):
		temp = self.head.next
		self.head =temp
		temp = None

	def reverselist(self):
		prev = None 
		current = self.head
		while(current!=None):
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev



print("Linkedlist FORMATION")
ll = Linkedlist()
ll.head = Node(2)
ll.head.next = Node(3)
ll.printlist()

print("ADD BEGIN")

ll.addbegin(12)
ll.addbegin(100)
ll.printlist()

print("add in between")

ll.addbetween(43,3)
ll.printlist()

print("add in the end of the list")

ll.addend(200)
ll.addend(201)

ll.printlist()

print("delete the first node")
ll.deletebeg()
ll.printlist()

print("Reversed List")
ll.reverselist()
ll.printlist()





