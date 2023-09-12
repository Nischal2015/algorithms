class BinarySearch:
  
  def __init__(self, list):
    self.list = list
    self.start = 0
    self.end = len(list) - 1

  def iterative_search(self, value):
    while(self.start <= self.end):
      middleValue = self.__getMiddleValue()

      if value == middleValue:
        return self.__getMiddleIndex()

      elif value < middleValue:
        self.end = self.__getMiddleIndex() - 1

      else:
        self.start = self.__getMiddleIndex() + 1

    raise Exception(f'{value} not found')

  def recursive_search(self, value):
    return self.__search(value, self.start, self.end)

  def __search(self, value, start, end):
    if start > end:
      raise Exception(f'{value} not found')

    middleValue = self.__getMiddleValue()
    if middleValue == value:
      return self.__getMiddleIndex()

    elif value < middleValue:
      self.end = self.__getMiddleIndex() - 1

    else:
      self.start = self.__getMiddleIndex() + 1 

    return self.__search(value, self.start, self.end)

  def __getMiddleIndex(self):
    return (self.start + self.end) // 2

  def __getMiddleValue(self):
    return self.list[self.__getMiddleIndex()]
