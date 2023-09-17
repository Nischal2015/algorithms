class ThreeGreatestNumber:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def __init__(self):
        self.threeGreatest = [0, 0, 0]

    def findThreeGreatest(self, array):
        for num in array:
            index = self.__returnGreaterThanIndex(num)
            if index:
                self.__shiftAndUpdate(num, index)

        return self.threeGreatest

    def __returnGreaterThanIndex(self, number):
        for i in range(2, -1, -1):
            if number > self.threeGreatest[i]:
                return i

    def __shiftAndUpdate(self, num, index):
        i = 0
        while i < index:
            self.threeGreatest[i] = self.threeGreatest[i+1]
            i += 1
        self.threeGreatest[i] = num


threeGreatestNumber = ThreeGreatestNumber()
print(threeGreatestNumber.findThreeGreatest(
    [144, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
