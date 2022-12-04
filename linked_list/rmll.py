class Node:
	def __init__(self,item):
		self.item = item
		self.next = None 

class LinkedList:
	def __init__(self):
		self.head = None 


	def insertatend(self,data):
		new_node = Node(data)
		if(self.head==None):
			self.head = new_node
			return

		temp = self.head
		while(temp.next!=None):
			temp = temp.next

		temp.next = new_node

	def printlist(self):
		temp = self.head
		while(temp!=None):
			print(temp.item,end=" ")
			temp = temp.next
		print()

	def removenodes(self,head):
		if(head==None):
			return None
		head.next = self.removenodes(head.next)
		if(head.next and head.item<head.next.item):
			return head.next
		else:
			return head
		# return head

	def removefirst(self):
		temp = self.head
		self.head = temp.next
		temp  = None 




llist = LinkedList()
llist.insertatend(4)
llist.insertatend(2)
llist.insertatend(5)
llist.insertatend(2)
llist.insertatend(13)
llist.insertatend(3)
llist.insertatend(8)
llist.printlist()
ll = LinkedList()


llist.removenodes(llist.head)
llist.removefirst()
llist.printlist()




