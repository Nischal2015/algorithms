class LongestPeak:
    def getLongestPeak(self, array):
        longestPeak = 0

        for i in range(1, len(array)-1):
            if self.__isPeak(i, array):
                tempLongestPeak = 3

                left = i - 1
                right = i + 1

                while left > 0 and array[left-1] < array[left]:
                    left -= 1
                    tempLongestPeak += 1

                while right < len(array)-1 and array[right+1] < array[right]:
                    right += 1
                    tempLongestPeak += 1

                longestPeak = max(longestPeak, tempLongestPeak)

        return longestPeak

    def __isPeak(self,  i, array):
        return array[i-1] < array[i] and array[i+1] < array[i]


longestPeak = LongestPeak()
print(longestPeak.getLongestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
