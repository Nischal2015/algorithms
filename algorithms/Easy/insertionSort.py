class InsertionSort:
    def sort(self, array):
        for i in range(1, len(array)):
            j = i
            currentItem = array[j]
            while currentItem < array[j-1] and j > 0:
                array[j] = array[j-1]
                j -= 1
            array[j] = currentItem

        return array


insertionSort = InsertionSort()
print(insertionSort.sort([456, 4, 2, 7, 8, 2, 12, 4,
      1, 42, 3, 1, 122, 3, 1, 34, 5]))
