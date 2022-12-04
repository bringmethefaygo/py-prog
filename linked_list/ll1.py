
class Node:
	def __init__(self,item):
		self.item = item
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insertatbeginning(self,newdata):
		new_node = Node(newdata)

		new_node.next = self.head
		self.head = new_node

	def insertatend(self,newdata):
		new_node = Node(newdata)

		if(self.head == None):
			self.head = new_node
			return

		last = self.head
		while(last.next):
			last = last.next
		last.next = new_node

	def deletenode(self,pos):
		if self.head == None:
			return

		temp = self.head
		while(pos>2):
			temp = temp.next
			pos = pos-1

		if temp is None:
			return
		if temp.next is None:
			return

		nxt = temp.next.next
		temp.next = None 
		temp.next = nxt 


	def printlist(self):
		temp = self.head
		while(temp!=None):
			print(temp.item,end="|")
			temp = temp.next
		print()

	
	def middlenode(self,head):
		fast = head
		slow = head
		while(fast.next != None and fast != None):
			fast = fast.next.next
			slow = slow.next
		return slow

	


llist = LinkedList()
llist.head = Node(12)
llist.insertatbeginning(4)
llist.insertatbeginning(10)

llist.insertatend(100)
llist.insertatend(101)

llist.printlist()

llist.deletenode(4)
llist.printlist()


llist.insertatend(2)
llist.printlist()

ll = LinkedList()
ll.head = llist.middlenode(llist.head)
ll.printlist()





