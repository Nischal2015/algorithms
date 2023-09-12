class BestDigits:
  def __init__(self, number, numDigits):
    self.number = number
    self.itemStack = []
    self.numDigits = numDigits

  def getBestDigits(self):
    for i in self.number:
      while self.__lengthOfStack() > 0 and self.__getLastItemFromStack() < i and self.numDigits > 0:
        self.numDigits -= 1
        self.itemStack.pop()

      self.itemStack.append(i)

    self.__popExtraItemsFromStack(self.numDigits)

    return self.__formatStackAsString()

  def __lengthOfStack(self):
    return len(self.itemStack)

  def __getLastItemFromStack(self):
    return self.itemStack[-1]
  
  def __popExtraItemsFromStack(self, numberOfItemsToPop):
    for _ in range(numberOfItemsToPop):
        self.itemStack.pop()

  def __formatStackAsString(self):
    return "".join(self.itemStack)
  
numbers = BestDigits("988762", 2)
print(numbers.getBestDigits())