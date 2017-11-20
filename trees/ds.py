stopMarker = "-1"

class TreeNode():
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def setData(self, data):
		self.data = data

	def setLeft(self, left):
		self.left = left

	def setRight(self, right):
		self.right = right

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def getData():
		return self.data

	def deserialize(root, tree,it):
		data = 0
		try:
			data = next(it)
			if data == stopMarker:
				return
		except StopIteration:
			return 

		tree.root = TreeNode(data)
		selfdeserialize(root.left, tree, it)
		deserialize(root.right, tree, it)

class Tree():
	def __init__(self, root):
		self.root = root
		self.data = []
		serialize(root, self)


def serialize(root, tree):
	if root == None:
		tree.data.append(stopMarker)
		return

	tree.data.append(str(root.data))
	serialize(root.left, tree)
	serialize(root.right, tree)

def deserialize(root, tree,it):
	data = 0
	try:
		data = next(it)
	except StopIteration:
		return None

	root = TreeNode(data)
	deserialize(root.left, tree, it)
	deserialize(root.right, tree, it)

def preorder_iter(root):
	if root == None:
		return

	nodes = []
	nodes.push(root)

	while not nodes:
		node = TreeNode(nodes.top())
		print(node.data)
		nodes.pop()

		if node.right:
			nodes.push(root.right.data)
		if node.left:
			nodes.push(root.left.data)

def deserialize_iter(root, it):
	temp = root
	stack_nodes = []
	data = 0
	
	try:
		data = next(it)
	except StopIteration:
		return None

	swi_flag = 'L'

	stack_nodes.push(data)

	parent = None
	while not stack_nodes:
		root = TreeNode(stack_nodes.top())
		stack_nodes.pop()

		try:
			data = next(serialized_iter)
			if data == stopMarker:
				if swi_flag == 'R':
					swi_flag = 'L'
				else:
					swi_flag = 'R'
				data = next(serialized_iter)
				if data == stopMarker:
					root = parent
		except StopIteration:
			return root



# def deserialize(node, it, tree, root):
# 	data = 0
# 	try:
# 		data = next(it)
# 		if data == stopMarker:
# 			return
# 	except StopIteration:
# 		return tree

# 	if root == True:
# 		tree.root = TreeNode(data)
# 		deserialize(tree.root.left, it, tree, False)
# 		deserialize(tree.root.right, it, tree, False)
# 	else:
# 		node = TreeNode(data)
# 		deserialize(node.left, it, tree, False)
# 		deserialize(node.right, it, tree, False)