from AlgorithmReusableComponents.BST.binarySearchTree import BinarySearchTree


class BranchSums:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def __init__(self, node):
        self.node = node
        self.sumList = []

    def calculateSums(self):
        self.__sum(self.node, 0, self.sumList)

        return self.sumList

    def __sum(self, node, runningSum, sumList):
        if node is None:
            return

        newRunningSum = runningSum + node.value
        if node.left is None and node.right is None:
            sumList.append(newRunningSum)
            return

        self.__sum(node.left, newRunningSum, sumList)
        self.__sum(node.right, newRunningSum, sumList)


array = BinarySearchTree([10, 5, 15, 2, 5, 13, 21, 1, 14])
tree = array.getBST()
branchSum = BranchSums(tree)
print(branchSum.calculateSums())
