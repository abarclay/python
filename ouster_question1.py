#!/usr/local/bin/python3
# you have a linked list with each node in the list having
# a unique id, a pointer to the next node, and an additional pointer which
# points to a random node in the list
# Write a function which, when passed a pointer to the head of the list,
# returns a deep copy

import random

class Node:
	def __init__(self,id):
		self.id=id
		self.next=None
		self.random=None

	def printList(self):
		if (self.next==None):
			return()
		print(self.id)
		self.next.printList()

	def printListRand(self):
		if (self.next==None):
			return()
		print(self.random.id)
		self.next.printListRand()

globhash={}
def buildglobhash(headNode):
	globhash[headNode.id] = headNode.random.id
	if (headNode.next == None):
		return(None)
	buildglobhash(headNode.next)

newhash={}
def buildnewhash(headNode):
	if (headNode == None):
		return(None)
	newhash[headNode.id] = headNode
	buildnewhash(headNode.next)

def setRandomPointer(headNode):
	if (headNode == None):
		return(None)
	# will return the id pointed to by the random pointer
	randid=globhash[headNode.id]
	headNode.random=newhash[randid]
	setRandomPointer(headNode.next)

def copyList(headNode):
	if (headNode == None):
		return(None)
	#print("creating new node with id " + str(headNode.id))
	newNode=Node(headNode.id)
	newNode.next=copyList(headNode.next)
	return(newNode)
		
def deepCopy(headNode):
	# run through once and create all the nodes
	newList=copyList(headNode)
	# build a global hash to indicate the id that the random ptr points to
	buildglobhash(headNode)
	# build a hash of the id and the node for the new list
	buildnewhash(newList)
	# now, run through the new list and set the random pointers for each
	# node
	setRandomPointer(newList)

	return(newList)

# build list
head=Node(3)
curr=head
for i in range(4,30):
	curr.next=Node(i)
	curr=curr.next

# initialize the random pointer to one of the existing nodes in the list
curr=head
for i in range(3,30):
	randNode=head
	rand=int(random.random()*25)
	#print("jumping foward " + str(rand) + " spaces")
	for j in range(1,rand):
		#print("next")
		randNode=randNode.next
	#print("setting randNode to node with id " + str(randNode.id))
	curr.random=randNode
	curr=curr.next

print("Here is the list of IDs of the nodes in the list")
head.printList()
print("---------------------")
print("Here is the list of IDs pointed to by the random pointers")
head.printListRand()

# now we have the list, make a deepCopy
newList=deepCopy(head)
#print(newList.id)
print("---------------------")
print("Here is the list of IDs of the nodes in the NEW list")
newList.printList()
print("Here is the list of IDs pointed to by the random pointers")
newList.printListRand()
