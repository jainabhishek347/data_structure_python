class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkList:
	def __init__(self, head):
		self.head = head

	def reverse(self):
		node = self.head
		current = None
		prev = None
		while(node):
			far = node.next 
			node.next = prev
			prev = node
			node = far

		self.head = prev

	def print_list(self):
		node = self.head
		while(node):
			print node.data
			node = node.next

	def mid_of_link_list(self):
		p2 = self.head
		p1 = self.head
		while(p2):
			p1 = p1.next
			p2 = p2.next.next

		print p1.data
n = Node(2)
link_list = LinkList(n)
n.next = Node(3)
n.next.next = Node(4)
n.next.next.next = Node(5)
link_list.print_list()
link_list.reverse()
print "reverse list"
link_list.print_list()

print "mid ele"
link_list.mid_of_link_list()