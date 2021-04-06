class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class Tree:
	def __init__(self):
		self.head = None

	def tree_traversal(self, node):
		#print node
		if node:
			self.tree_traversal(node.left)
			print node.data
			self.tree_traversal(node.right)

	def pre_tree_traversal(self, node):
		if node:
			print node.data
			self.tree_traversal(node.left)
			self.tree_traversal(node.right)

	def post_tree_traversal(self, node):
		if node:
			self.tree_traversal(node.left)
			self.tree_traversal(node.right)
			print node.data

	def reverse_tree(self, node):
		if node:
			
			self.reverse_tree(node.left)
			
			self.reverse_tree(node.right)
			temp = node.left
			node.left = node.right
			node.right = temp

n = Node(100)
tree = Tree()
tree.head=n
n = Node(200)
tree.head.right = n
n = Node(20)
tree.head.left = n
n = Node(230)
tree.head.right.right = n
n = Node(190)
tree.head.right.left = n
print "In order traversal"
#tree.tree_traversal(tree.head)
print "Pre order traversal"
#tree.pre_tree_traversal(tree.head)
print "Post order traversal"
#tree.post_tree_traversal(tree.head)

print "tree reverse:"
tree.reverse_tree(tree.head)
tree.tree_traversal(tree.head)
