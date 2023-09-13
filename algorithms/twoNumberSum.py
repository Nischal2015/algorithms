class TwoNumberSum:
  def __init__(self, arrayOfNumbers, target):
    self.arrayOfNumbers = arrayOfNumbers
    self.target = target
    self.left = 0
    self.right = len(arrayOfNumbers) - 1
    self.hashMap = {}

  def sumUsingNestedLoop(self):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    for i in range(len(self.arrayOfNumbers)-1):
      firstNumber = self.arrayOfNumbers[i]
      for j in range(i+1, len(self.arrayOfNumbers)):
        secondNumber = self.arrayOfNumbers[j]
        if firstNumber + secondNumber == self.target:
          return [firstNumber, secondNumber]

  def sumUsingHashMap(self):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    for number in self.arrayOfNumbers:
      complement = self.target - number
      if complement in self.hashMap.keys():
        return [number, complement]
      else:
        self.hashMap[number] = True

  def sumUsingTwoPointers(self):
    """
    Time Complexity: O(n*log(n))
    Space Complexity: O(1)
    """

    sortedArrayOfNumbers = sorted(self.arrayOfNumbers)
    while(self.left < self.right):
      numberOnLeftIndex = sortedArrayOfNumbers[self.left]
      numberOnRightIndex = sortedArrayOfNumbers[self.right]
      sumOfNumbers = numberOnLeftIndex + numberOnRightIndex
      if sumOfNumbers == self.target:
        return [numberOnLeftIndex, numberOnRightIndex]
      
      elif sumOfNumbers < self.target:
        self.left += 1

      else:
        self.right -= 1
  
twoNumberSum = TwoNumberSum([-1,11,3,6,5,-4,8,1], 10)
print(twoNumberSum.sumUsingNestedLoop())
print(twoNumberSum.sumUsingHashMap())
print(twoNumberSum.sumUsingTwoPointers())