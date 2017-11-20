import ds

def main():
	root = ds.TreeNode(20)
	root.left = ds.TreeNode(8)
	root.right = ds.TreeNode(22)
	root.left.left = ds.TreeNode(4) 
	root.left.right = ds.TreeNode(12); 
	root.left.right.left = ds.TreeNode(10); 
	root.left.right.right = ds.TreeNode(14);

	tree = ds.Tree(root)
	print(tree.data)

	copyRoot = ds.TreeNode(None)
	copyRoot.deserialize(iter(tree.data))
	copyTree = ds.Tree(copyRoot)
	print(copyTree.data)


if __name__ == '__main__':
	main()