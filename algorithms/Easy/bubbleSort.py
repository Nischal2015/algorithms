class BubbleSort:
    def sort(self, array):
        arrayLength = len(array)
        for i in range(arrayLength):
            for j in range(arrayLength-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]

        return array


bubbleSort = BubbleSort()
print(bubbleSort.sort([456, 4, 2, 7, 8, 2, 12, 4,
      1, 42, 3, 1, 122, 3, 1, 34, 5]))
