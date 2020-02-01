#!/usr/bin/python

class Node:
	def __init__(self,data=None):
		self.left = None
		self.right = None
		self.data = data

	def insert(self,data):
		if (self.data is None):
			self.data = data
		else:
			if (data < self.data):
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			if (data >= self.data):
				if (self.right is None):
					self.right = Node(data)
				else:
					self.right.insert(data)

	def printTree(self):
		if (self.left is not None):
			self.left.printTree()
		if (self.data is not None):
			print self.data
		if (self.right is not None):
			self.right.printTree()

# main
foo = Node()
foo.printTree()
foo.insert(4)
foo.printTree()

print("\n")

root = Node(12)
root.insert(3)
root.insert(3)
root.insert(6)
root.insert(9)
root.insert(15)

root.printTree()
