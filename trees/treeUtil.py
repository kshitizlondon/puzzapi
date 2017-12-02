from trees import ds


def getPathFromRoot(root, path, n):
	if root == None:
		return False

	path.append(root)

	if root.data == n:
		return True

	if (root.left != None and getPathFromRoot(root.left, path, n)) or (root.right != None and getPathFromRoot(root.right, path, n)):
		return True

	path = path[0:len(path)-1]
	return False

def getLCAHelper(root, n1, n2):
	if root == None:
		return None

	if root.data == n1 or root.data == n2:
		return root

	lefty = getLCAHelper(root.left, n1, n2)
	righty = getLCAHelper(root.right, n1, n2)

	if lefty != None and righty != None:
		return root

	if lefty != None:
		return lefty
	else:
		return righty

def getLCA(serialized_tree, n1, n2):
	tree_root = ds.TreeNode(None)
	ds.deserialize(tree_root, iter(serialized_tree))
	tree = ds.Tree(tree_root)
	
	path = []
	getPathFromRoot(tree.root, path, str(n1))
	if len(path) == 0:
		return None

	getPathFromRoot(tree.root, path, str(n2))
	if len(path) == 0:
		return None

	return getLCAHelper(tree.root, str(n1), str(n2))