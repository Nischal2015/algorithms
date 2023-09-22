class ArrayOfProducts:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def arrayOfProducts(self, array):
        arrayLength = len(array)
        self.productArray = [1] * arrayLength

        self.__multiplierArrayGenerator(array)
        self.__multiplierArrayGenerator(array, reverse=True)

        return self.productArray

    def __multiplierArrayGenerator(self, array, reverse=False):
        product = 1
        if reverse:
            iteratorArray = reversed(list(enumerate(array)))
        else:
            iteratorArray = enumerate(array)

        for i, item in iteratorArray:
            self.productArray[i] *= product
            product *= item


arrayOfProducts = ArrayOfProducts()
print(arrayOfProducts.arrayOfProducts([7, 3, 4, 2,]))
