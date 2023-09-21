class MonotonicArrays:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def isMonotonic(self, array):
        arrayLength = len(array)

        if arrayLength <= 2:
            return True

        firstIdx = 1
        while array[firstIdx-1] == array[firstIdx]:
            firstIdx += 1
            if firstIdx == arrayLength:
                return True

        direction = 1 if array[firstIdx-1] < array[firstIdx] else -1
        while firstIdx < arrayLength:
            if direction * array[firstIdx-1] > direction * array[firstIdx]:
                return False
            firstIdx += 1
        return True


monotonicArrays = MonotonicArrays()
print(monotonicArrays.isMonotonic(
    [-1, -1, -1, -2, -3, -4]))
