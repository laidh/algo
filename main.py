
class TreeNode(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.height = 1

class AVL_Tree(object):
	def insert(self, root, key):
		if not root:
			return TreeNode(key)
		elif key < root.value:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)

		root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))


		balance = self.getBalance(root)

		if balance > 1 and key < root.left.value:
			return self.rightRotate(root)

		if balance < -1 and key > root.right.value:
			return self.leftRotate(root)

		if balance > 1 and key > root.left.value:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		if balance < -1 and key < root.right.value:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root

	def leftRotate(self, z):

		y = z.right
		R2 = y.left

		y.left = z
		z.right = R2

		z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		return y

	def rightRotate(self, z):

		y = z.left
		R3 = y.right

		y.right = z
		z.left = R3

		z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		return y

	def getHeight(self, root):
		if not root:
			return 0

		return root.height

	def getBalance(self, root):
		if not root:
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right)

	def preOrder(self, root):

		if not root:
			return

		print("{0} ".format(root.value), end="")
		self.preOrder(root.left)
		self.preOrder(root.right)


myTree = AVL_Tree()
root = None

root = myTree.insert(root, 5)
root = myTree.insert(root, 20)
root = myTree.insert(root, 15)

myTree.preOrder(root)
