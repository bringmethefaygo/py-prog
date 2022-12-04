

class Node:
	def __init__(self,item):
		self.item = item
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

linked_list = LinkedList()
linked_list.head = Node(112)
second = Node(22)
third = Node(4)

linked_list.head.next = second
second.next = third

print(linked_list.head)
aff = linked_list.head
while(aff != None):
	print(aff.item,end =" ")
	aff = aff.next
print()
print(linked_list.head)