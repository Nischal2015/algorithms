class TandemBicycle:
  """
  Time Complexity: O(n*log(n))
  Space Complexity: O(n)
  """

  def __init__(self, redShirtSpeeds, blueShirtSpeeds, fastest):
    self.redShirtSpeeds = redShirtSpeeds
    self.blueShirtSpeeds = blueShirtSpeeds
    self.fastest = fastest

  def tandemBicycleSpeed(self):
    totalScore = 0

    redShirtSpeedsSorted = sorted(self.redShirtSpeeds)
    blueShirtSpeedsSorted = sorted(self.blueShirtSpeeds, reverse=self.fastest)

    for i in range(len(redShirtSpeedsSorted)):
      totalScore += max(redShirtSpeedsSorted[i], blueShirtSpeedsSorted[i])

    return totalScore
  
redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
tandemBicycle = TandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest=False)
print(tandemBicycle.tandemBicycleSpeed())