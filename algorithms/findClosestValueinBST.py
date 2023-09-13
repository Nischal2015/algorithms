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


class FindClosestValueInBST:
    def __init__(self, binaryTree):
        self.binaryTree = binaryTree
        self.closestDistance = float('inf')
        self.closestValue = None

    def findClosestValue(self, targetValue):
        self.__find(self.binaryTree, targetValue)

        return self.closestValue

    def __find(self, tree, targetValue):
        if tree is None:
            return self.closestValue

        if abs(targetValue - tree.value) < self.closestDistance:
            self.closestValue = tree.value
            self.closestDistance = abs(targetValue - tree.value)

        if targetValue < tree.value:
            return self.__find(tree.left, targetValue)
        elif targetValue > tree.value:
            return self.__find(tree.right, targetValue)
        else:
            return self.closestValue


array = BinarySearchTree([10, 5, 15, 2, 5, 13, 21, 1, 14])
tree = array.getBST()
closestValue = FindClosestValueInBST(tree)
print(closestValue.findClosestValue(12))
