from collections import defaultdict

class TierNode(object):
	def __init__(self, key=None, count=0):
		self.children = defaultdict()
		self.is_leaf = False
		if key:
			self.children[key] =count



class Trie(object):
	def __init__(self, node):
		self.root = node

	def insert(self, str):
		r = self.root
		for s in str:
			if s not in r.children:
				r.children[s]=TierNode()

			r.children[s] = r.children[s]+1
			r = r.children[s]
		r.is_leaf =True

	def search(self, str):
		r = self.root
		for s in str:
			if s in r.children:
				r = r.children[s]
			else:
				return False

		return True if r.is_leaf else False

string = ["abhi", "ram", "abhishek", "abhish"]

tn = TierNode() 
tr = Trie(tn)
for s in string:
	tr.insert(s)
print tr.search("abhi")
print tr.search("abhidsds")
print tr.search("abhishek")
print tr.search("abhish")
print tr.search("abhis")
print tr.search("abhishekk")