class ClassPhotos:
    """
    Time Complexity: O(n*log(n))
    Space Complexity: O(n)
    """

    def __init__(self, redShirtList, blueShirtList):
        self.redShirtList = redShirtList
        self.blueShirtList = blueShirtList

    def canArrangeClassPhoto(self):
        redShirtSorted = sorted(self.redShirtList, reverse=True)
        blueShirtSorted = sorted(self.blueShirtList, reverse=True)

        redShirtHasMaxHeight = redShirtSorted[0] > blueShirtSorted[0]

        for i in range(len(redShirtSorted)):
            if redShirtHasMaxHeight and blueShirtSorted[i] > redShirtSorted[i]:
                return False
            elif not redShirtHasMaxHeight and redShirtSorted[i] > blueShirtSorted[i]:
                return False

        return True


redShirt = [5, 8, 1, 3, 4]
blueShirt = [6, 9, 2, 4, 5]

classPhotos = ClassPhotos(redShirt, blueShirt)
print(classPhotos.canArrangeClassPhoto())
