class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # insert a node into the tree
    def insert(self, data):
        node = TreeNode(data)
        if self.root is None:
            self.root = node
        else:
            self._insert(self.root, data)

    # insert node recursively
    def _insert(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = TreeNode(data)
            else:
                self._insert(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(data)
            else:
                self._insert(current_node.right, data)

    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, traversal):
        if node:
            self._inorder_traversal(node.left, traversal)
            traversal.append(node.data)
            self._inorder_traversal(node.right, traversal)
        return traversal

    def preorder_traversal(self):
        return self._preorder_traversal(self.root, [])

    def _preorder_traversal(self, node, traversal):
        if node:
            traversal.append(node.data)
            self._preorder_traversal(node.left, traversal)
            self._preorder_traversal(node.right, traversal)
        return traversal

    def postorder_traversal(self):
        return self._postorder_traversal(self.root, [])

    def _postorder_traversal(self, node, traversal):
        if node:
            self._postorder_traversal(node.left, traversal)
            self._postorder_traversal(node.right, traversal)
            traversal.append(node.data)
        return traversal

tree = BinaryTree()
tree.insert(10)
tree.insert(25)
tree.insert(30)
tree.insert(45)
tree.insert(13)

print("Inorder traversal: ", tree.inorder_traversal())
print("Preorder traversal: ", tree.preorder_traversal())
print("Postorder traversal: ", tree.postorder_traversal())