class BestSeat:
  def __init__(self, seatArrangement):
    self.seatArrangement = seatArrangement
    self.bestSeat = -1
    self.maxSpace = 0
    self.left = 0
    self.right = 0

  def getBestSeat(self):
    while self.left < len(self.seatArrangement):
      self.right = self.left + 1

      while self.right < self.__lengthOfSeatArrangement() and self.seatArrangement[self.right] != 1:
        self.right += 1

      availableSeat = self.right - self.left - 1
      if availableSeat > self.maxSpace:
        self.bestSeat = (self.right + self.left) // 2
        self.maxSpace = availableSeat

      self.left = self.right
     
    return self.bestSeat
  
  def __lengthOfSeatArrangement(self):
    return len(self.seatArrangement)
  
seat = BestSeat([1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1])
print(seat.getBestSeat());
