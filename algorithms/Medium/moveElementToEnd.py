class MoveElementToEnd:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def move(self, array, target):
        firstIdx = 0
        lastIdx = len(array)-1

        while firstIdx < lastIdx:
            while array[lastIdx] == target:
                lastIdx -= 1

            while array[firstIdx] != target:
                firstIdx += 1

            if firstIdx < lastIdx:
                array[firstIdx], array[lastIdx] = array[lastIdx], array[firstIdx]

            firstIdx += 1

        return array

    # def move(self, array, target):
    #     lastIdx = len(array)-1

    #     while firstIdx < lastIdx:
    #         while firstIdx < lastIdx and array[lastIdx] == target:
    #             lastIdx -= 1

    #         if array[firstIdx] == target:
    #             array[firstIdx], array[lastIdx] = array[lastIdx], array[firstIdx]

    #         firstIdx += 1

    #     return array


moveElementToEnd = MoveElementToEnd()
print(moveElementToEnd.move(
    [2, 2, 4, 5, 6, 23, 2, 2, 2, 2, 3, 4, 2], 2))
