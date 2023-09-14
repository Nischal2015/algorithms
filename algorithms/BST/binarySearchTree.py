class BSTNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self, array):
        self.array = array
        self.tree = None

    def getBST(self):
        self.__constructBST()

        return self.tree

    def insert(self, tree, value):
        if tree is None:
            return BSTNode(value)

        if value < tree.value:
            tree.left = self.insert(tree.left, value)
        else:
            tree.right = self.insert(tree.right, value)
        return tree

    def __constructBST(self):
        for i in self.array:
            self.tree = self.insert(self.tree, i)
