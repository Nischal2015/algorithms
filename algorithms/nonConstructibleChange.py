class NonConstructibleChange:
    """
    Time Complexity: O(n*log(n))
    Space complexity: O(n)

    Space Complexity can be reduced to O(1) by using in-place sorting
    """

    def __init__(self, array):
        self.array = array

    def getChange(self):
        sortedArray = sorted(self.array)
        currentChangeCreated = 0

        for coin in sortedArray:
            if coin > currentChangeCreated + 1:
                return currentChangeCreated + 1

            currentChangeCreated += coin

        return currentChangeCreated + 1


array = NonConstructibleChange([5, 7, 1, 1, 2, 3, 22])
print(array.getChange())
