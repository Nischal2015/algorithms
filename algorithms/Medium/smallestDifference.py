class SmallestDifference:
    """
    Time Complexity: O(n*log(n)) + O(m*log(m))
    Space Complexity: O(n+m)

    n = Length of first array
    m = Length of second array
    """

    def getSmallestDifferenceArray(self, firstArray, secondArray):
        sortedFirstArray = sorted(firstArray)
        sortedSecondArray = sorted(secondArray)

        smallestDifference = float('inf')
        smallestDifferenceArray = []

        firstArrayIdx = 0
        secondArrayIdx = 0
        while firstArrayIdx < len(sortedFirstArray) and secondArrayIdx < len(sortedSecondArray):
            firstArrayIdxNumber = sortedFirstArray[firstArrayIdx]
            secondArrayIdxNumber = sortedSecondArray[secondArrayIdx]
            absoluteDifference = abs(
                firstArrayIdxNumber - secondArrayIdxNumber)

            if absoluteDifference < smallestDifference:
                smallestDifference = absoluteDifference
                smallestDifferenceArray = [
                    firstArrayIdxNumber, secondArrayIdxNumber]

            if firstArrayIdxNumber < secondArrayIdxNumber:
                firstArrayIdx += 1
            elif firstArrayIdxNumber > secondArrayIdxNumber:
                secondArrayIdx += 1
            else:
                return smallestDifferenceArray

        return smallestDifferenceArray


firstArray = [-1, 5, 10, 20, 28, 3]
secondArray = [26, 134, 135, 15, 17]
smallestDifference = SmallestDifference()
print(smallestDifference.getSmallestDifferenceArray(firstArray, secondArray))
