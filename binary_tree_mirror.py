# Python program to find the maximum depth of tree
 
# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Compute the "maxDepth" of a tree -- the number of nodes 
# along the longest path from the root node down to the 
# farthest leaf node
def mirror(node):
    if node is None:
        return None
    else :
        temp =node.left
        node.left = node.right
        node.right = temp
        lDepth = mirror(node.left)
        rDepth = mirror(node.right)
        #print path
def inorder_traverse(node):
    if node is None:
        return

    if node.left is not None:
        inorder_traverse(node.left)

    print node.data

    if node.right is not None: 
        inorder_traverse(node.right) 
 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
inorder_traverse(root)
mirror(root)
print "====="*4
inorder_traverse(root)
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)