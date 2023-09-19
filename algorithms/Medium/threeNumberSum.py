class ThreeNumberSum:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """

    def calculate(self, numberList, target):
        threeNumberList = []
        sortedNumberList = sorted(numberList)

        for i in range(len(sortedNumberList)-2):
            leftIdx = i+1
            rightIdx = len(sortedNumberList) - 1
            while leftIdx < rightIdx:
                currentIdxNumber = sortedNumberList[i]
                leftIdxNumber = sortedNumberList[leftIdx]
                rightIdxNumber = sortedNumberList[rightIdx]
                currentSum = currentIdxNumber + leftIdxNumber + rightIdxNumber

                if currentSum > target:
                    rightIdx -= 1
                elif currentSum < target:
                    leftIdx += 1
                else:
                    threeNumberList.append(
                        [currentIdxNumber, leftIdxNumber, rightIdxNumber])
                    rightIdx -= 1
                    leftIdx += 1
        return threeNumberList


threeNumberSum = ThreeNumberSum()
print(threeNumberSum.calculate([12, 3, 1, 2, -6, 5, -8, 6], 0))
