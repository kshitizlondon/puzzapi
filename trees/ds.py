stopMarker = "-1"

class TreeNode():
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	
	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def getData():
		return self.data

	def setData(self, data):
		if self == None:
			self = TreeNode(data)
		else:
			self.data = data

	def setLeft(self, left):
		if left == None:
			self.left = None
		else:
			self.left = TreeNode(left.data)

	def setRight(self, right):
		if right == None:
			self.right = None
		else:
			self.right = TreeNode(right.data)

class Tree():
	def __init__(self, root):
		self.root = root
		self.data = []
		serialize(root, self)


def serialize(root, tree):
	if root == None or root.data == None:
		tree.data.append(stopMarker)
		return

	tree.data.append(str(root.data))
	serialize(root.left, tree)
	serialize(root.right, tree)

def deserialize(root, it):
	data = 0
	try:
		data = next(it)
		if data == stopMarker:
			return None
	except StopIteration:
		return None

	if root == None:
		root = TreeNode(None)

	root.data = data
	root.left = deserialize(root.left, it)
	root.right = deserialize(root.right, it)
	return root