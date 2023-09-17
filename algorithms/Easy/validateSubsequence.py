class ValidateSubsequence:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def __init__(self, sourceArray, subsequenceArray):
        self.sourceArray = sourceArray
        self.subsequenceArray = subsequenceArray
        self.sourceArrayIndex = 0
        self.subsequenceArrayIndex = 0

    def validate(self):
        while self.subsequenceArrayIndex < len(self.subsequenceArray) and self.sourceArrayIndex < len(self.sourceArray):
            if self.subsequenceArray[self.subsequenceArrayIndex] == self.sourceArray[self.sourceArrayIndex]:
                self.subsequenceArrayIndex += 1
            self.sourceArrayIndex += 1

        return self.subsequenceArrayIndex == len(self.subsequenceArray)


array = ValidateSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, 10, -1])
print(array.validate())
