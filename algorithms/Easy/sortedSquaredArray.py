class SortedSquaredArray():
    def __init__(self, array):
        self.array = array

    def sortSquaredBruteForce(self):
        """
        Time Complexity: O(n*log(n))
        Space Complexity: O(n)
        """

        squaredArray = [i**2 for i in self.array]
        return sorted(squaredArray)

    def sortSquaredOptimizedSort(self):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        self.leftIndex = 0
        self.rightIndex = len(self.array) - 1
        reverseIndex = len(self.array) - 1

        sortedSquares = [0 for _ in self.array]
        while (self.leftIndex <= self.rightIndex):
            absValueAtLeftIndex = self.__getAbsoluteValueAtIndex(
                self.leftIndex)
            absValueAtRightIndex = self.__getAbsoluteValueAtIndex(
                self.rightIndex)

            if absValueAtLeftIndex < absValueAtRightIndex:
                sortedSquares[reverseIndex] = self.__getSquareAtIndex(
                    self.rightIndex)
                self.rightIndex -= 1
            else:
                sortedSquares[reverseIndex] = self.__getSquareAtIndex(
                    self.leftIndex)
                self.leftIndex += 1

            reverseIndex -= 1

        return sortedSquares

    def __getSquareAtIndex(self, index):
        return self.array[index] ** 2

    def __getAbsoluteValueAtIndex(self, index):
        return abs(self.array[index])


sortedSquaredArray = SortedSquaredArray([-5, -4, 3, 6, 7, 8, 9])
print(sortedSquaredArray.sortSquaredBruteForce())
print(sortedSquaredArray.sortSquaredOptimizedSort())
