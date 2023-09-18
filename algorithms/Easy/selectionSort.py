class SelectionSort:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def sort(self, array):
        smallestElementIndex = 0

        arrayLength = len(array)
        for i in range(arrayLength):
            for j in range(i+1, arrayLength):
                if array[j] < array[smallestElementIndex]:
                    smallestElementIndex = j
            self.__swap(i, smallestElementIndex, array)

        return array

    def __swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]


selectionSort = SelectionSort()
print(selectionSort.sort([8, 5, 2, 9, 5, 6, 3]))
