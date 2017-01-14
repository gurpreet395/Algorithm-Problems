
# Node class
class Node:

	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

# Tree class
class BTree:

	def __init__(self,id):
		self.root=id
		
		self.left=None
		self.right=None

	def addLeftChild(self,lchild):
		if self.left==None:
			self.left=BTree(lchild)
		else:
			tree=BTree(lchild)
			tree.left=self.left
			self.left=tree

	def addRightChild(self,rchild):
		if self.right==None:
			self.right=BTree(rchild)
		else:
			tree=BTree(rchild)
			tree.right=self.right
			self.right=tree
	
	def getLeftChild(self):
		if self.left!=None:
			return self.left

	def getRightChild(self):
		if self.right!=None:
			return self.right

	def getValue(self):
		return self.root


G=BTree(1)
G.addLeftChild(2)
G.addRightChild(3)
G.addLeftChild(4)
G.addRightChild(5)
G.addLeftChild(6)
G.addRightChild(7)

##----------------------------

#Print graprh (Pre-order Traversal)
#---------------------------------

def preorder(Graph):
	if (Graph==None):
		return
	else:
		print Graph.getValue()
		#print Graph.getLeftChild()
		if (Graph.getLeftChild !=None):
			 preorder(Graph.getLeftChild())

		if(Graph.getRightChild !=None):
			preorder(Graph.getRightChild())
	#else:
		#if(Graph.getrightChild !=None):
		#:wq
	#return preorder(Graph.getLeftChild())

preorder(G)
	







 


	
	
		
	