class MinimumWaitingTime:
  """
  Time Complexity: O(n*log(n))
  Space Complexity: O(n)
  """

  def __init__(self, timeArray):
    self.timeArray = timeArray

  def calculateTime(self):
    sortedTimeArray = sorted(self.timeArray)
    minimumWaitingTime = 0

    for index, num in enumerate(reversed(sortedTimeArray)):
      minimumWaitingTime += index * num

    return minimumWaitingTime

waitingTime = MinimumWaitingTime([3,2,1,2,6])
print(waitingTime.calculateTime())