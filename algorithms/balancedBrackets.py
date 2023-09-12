class BalancedBrackets:

  def __init__(self, bracketList):
    self.bracketList = bracketList
    self.bracketStack = []
    self.openingBrackets = ['[', '{', '(']
    self.closingBrackets = [']', '}', ')']
    self.bracketMapping = {']': '[', '}': '{', ')': '('}

  def isBalanced(self):
    for i in self.bracketList:
      if i in self.openingBrackets:
        self.bracketStack.append(i)
      
      elif i in self.closingBrackets:
        stackEmpty = self.__isEmpty();
        bracketNotMatching = self.bracketStack.pop() != self.bracketMapping[i]
        if stackEmpty or bracketNotMatching:
          return False
      
      else:
        raise Exception(f'{i} is not a desired bracket')
    
    return self.__isEmpty();

  def __isEmpty(self):
    return not bool(len(self.bracketStack))

bracket = BalancedBrackets(['[', '{', '(', ')', '}', ']', ','])
print(bracket.isBalanced())