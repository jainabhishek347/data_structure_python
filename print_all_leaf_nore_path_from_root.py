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
def print_leaf_path(node, p=None):
    #print "node.data", node.data     
    if not p:
        path =[]
    else:
        path = list(p)
    if node is None:
        return path
    else :
        path.append(node.data)
        if node.left is None and node.right is None:
            print path
        # Compute the depth of each subtree
        lDepth = print_leaf_path(node.left,path)
        rDepth = print_leaf_path(node.right, path)
        #print path

 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
 
print_leaf_path(root)
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)