class ProductSum:
    """
    Time Complexity: O(N)
    Space Complexity: O(d)

    N = Total number of elements in array including all of elements in each sub-array
    d = Max depth of array
    """

    def calculate(self, array, multiplier=1):
        sum = 0
        for element in array:
            if isinstance(element, int):
                sum += element
            else:
                sum += self.calculate(element, multiplier+1)
        return sum * multiplier


prodSum = ProductSum()
print(prodSum.calculate([5, 2, [7, -1], 3, [6, [-13, 7], 4]]))
