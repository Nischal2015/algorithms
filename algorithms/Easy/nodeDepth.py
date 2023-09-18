from AlgorithmReusableComponents.BST.binarySearchTree import BinarySearchTree


class NodeDepth:
    """
    Time Complexity: O(n)
    Space Complexity: O(h)
    """

    def __init__(self, tree):
        self.tree = tree

    def sumOfNodeDepth(self):
        return self.__sum(self.tree, 0)

    def __sum(self, tree, depth):
        if tree is None:
            return 0

        return depth + self.__sum(tree.left, depth + 1) + self.__sum(tree.right, depth + 1)


array = BinarySearchTree([10, 5, 15, 2, 5, 13, 21, 1, 14, 12])
tree = array.getBST()
nodeDepth = NodeDepth(tree)
print(nodeDepth.sumOfNodeDepth())
