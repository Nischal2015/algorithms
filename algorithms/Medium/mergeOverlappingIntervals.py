class MergeOverLappingIntervals:
    """
    Time Complexity: O(n*log(n))
    Space Complexity: O(n)
    """

    def merge(self, array):
        sortedArray = sorted(array)
        mergedArray = []

        currentInterval = sortedArray[0]
        mergedArray.append(currentInterval)

        for nextItem in sortedArray[1:]:
            _, currentIntervalEnd = currentInterval
            nextIntervalStart, nextIntervalEnd = nextItem

            if currentIntervalEnd >= nextIntervalStart:
                currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
            else:
                currentInterval = nextItem
                mergedArray.append(currentInterval)

        return mergedArray


mergeOverLappingIntervals = MergeOverLappingIntervals()
print(mergeOverLappingIntervals.merge(
    [[1, 2], [3, 5], [6, 8], [4, 7], [9, 15], [10, 13]]))
