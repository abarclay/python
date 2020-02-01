#!/usr/bin/python

# try to implement the binary sort without objects or trees

next=0

def insert(mynode, data):
   global next
   if (mynode["data"] is None):
     mynode["data"] = data
     return
   if (data < mynode["data"]):
	if (mynode["left"] is None):
          next = next + 1
	  mynode["left"] = next
	  x[next]["data"] = data
	else:
          next = next + 1
	  insert(mynode[next],data)
   if (data >= mynode["data"]):
	if (mynode["right"] is None):
          next = next + 1
	  mynode["right"] = next
	  x[next]["data"] = data
	else:
          next = next + 1
	  insert(mynode[next],data)

def printTree(mytree):
	if (mytree["left"] is not None):
	  printTree(mytree["left"])
	
	print(mytree["data"])

	if (mytree["right"] is not None):
	  printTree(mytree["right"])

node = {
  "left": None,
  "right": None,
  "data": None,
}

x=[node]*4096

x[next]=node

insert(x[0],12)
insert(x[0],3)

#root.insert(3)
#root.insert(6)
#root.insert(9)
#root.insert(15)

printTree(x[0])
