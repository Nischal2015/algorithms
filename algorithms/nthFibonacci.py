class NthFibonacci:
    def __init__(self):
        self.memoizedHashMap = {1: 0, 2: 1}

    def getNthNumberRecursiveNaive(self, number):
        """
        Time Complexity: O(2^n)
        Space Complexity: O(n)
        """

        self.__checkForNumberEligibility(number)
        if self.__checkBaseCase(number):
            return number - 1

        return self.getNthNumberRecursiveNaive(number-1) + self.getNthNumberRecursiveNaive(number-2)

    def getNthNumberRecursiveOptimized(self, number):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        self.__checkForNumberEligibility(number)
        if self.__checkBaseCase(number):
            return number - 1

        return self.__recursiveOptimizedHelper(number, self.memoizedHashMap)

    def getNthNumberIterative(self, number):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        if self.__checkBaseCase(number):
            return number - 1

        currentNumber = 0
        nextNumber = 1
        for _ in range(number-2):
            sum = currentNumber + nextNumber
            currentNumber = nextNumber
            nextNumber = sum
        return sum

    def __recursiveOptimizedHelper(self, number, memoize):
        if number in memoize:
            return memoize[number]
        else:
            memoize[number] = self.getNthNumberRecursiveOptimized(
                number-1) + self.getNthNumberRecursiveOptimized(number-2)
            return memoize[number]

    def __checkForNumberEligibility(self, number):
        if number <= 0:
            raise Exception("Number cannot be less than 1")

    def __checkBaseCase(self, number):
        return number >= 1 and number <= 2


fibonacci = NthFibonacci()
print(fibonacci.getNthNumberRecursiveOptimized(8))
print(fibonacci.getNthNumberRecursiveOptimized(9))
print(fibonacci.getNthNumberRecursiveOptimized(10))
