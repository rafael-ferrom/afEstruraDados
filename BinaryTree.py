from NodeTree import NodeTree

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, id, name):
        self.root = self._insert_rec(self.root, id, name)

    def _insert_rec(self, root, id, name):
        if root is None:
            return NodeTree(id, name)
        if id < root.id:
            root.left = self._insert_rec(root.left, id, name)
        elif id > root.id:
            root.right = self._insert_rec(root.right, id, name)
        return root

    def search(self, id):
        steps = 0
        result, steps = self._search_rec(self.root, id, steps)
        return result, steps

    def _search_rec(self, root, id, steps):
        steps += 1
        if root is None or root.id == id:
            return root, steps
        elif id < root.id:
            return self._search_rec(root.left, id, steps)
        else:
            return self._search_rec(root.right, id, steps)

    def inorder(self):
        return self._inorder_rec(self.root)

    def _inorder_rec(self, root):
        result = []
        if root:
            result = self._inorder_rec(root.left)
            result.append((root.id, root.name))
            result = result + self._inorder_rec(root.right)
        return result
