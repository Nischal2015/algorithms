class SpiralTraverse:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    n = Total no. of elements in 2D array
    """

    def traverse(self, array):
        startRow, endRow = 0, len(array)-1
        startColumn, endColumn = 0, len(array[0])-1
        result = []

        while startColumn <= endColumn and startRow <= endRow:
            for col in range(startColumn, endColumn+1):
                result.append(array[startRow][col])

            for row in range(startRow+1, endRow+1):
                result.append(array[row][endColumn])

            for col in range(endColumn-1, startColumn-1, -1):
                result.append(array[endRow][col])

            for row in range(endRow-1, startRow, -1):
                result.append(array[row][startColumn])

            startColumn += 1
            startRow += 1
            endColumn -= 1
            endRow -= 1

        return result


matrix = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7],
    ["a", "b", "c", "d"]
]
spiralTraverse = SpiralTraverse()
print(spiralTraverse.traverse(matrix))
