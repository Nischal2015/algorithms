class FirstDuplicateValue:
    def duplicateValue(self, array):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        seen = set()
        for item in array:
            if item in seen:
                return item
            seen.add(item)

        return -1

    def inPlaceDuplicateValue(self, array):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)

        This method only work if the array is from 1...n and in-place substitution is allowed
        """

        for num in array:
            numAbsolute = abs(num)
            if array[numAbsolute-1] < 0:
                return numAbsolute
            array[numAbsolute-1] *= -1

        return -1


firstDuplicateValue = FirstDuplicateValue()
print(firstDuplicateValue.inPlaceDuplicateValue([2, 1, 5, 3, 3, 2, 4]))
print(firstDuplicateValue.duplicateValue([2, 3, 1, 5, 3, 3, 2, 4]))
