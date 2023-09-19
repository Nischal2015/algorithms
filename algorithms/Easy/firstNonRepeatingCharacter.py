class FirstNonRepeatingCharacter:
    def __init__(self):
        self.countsHashTable = {}

    def optimizedApproach(self, characterList):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        self.__createCharacterCountHashTable(characterList)
        return self.__findFirstKeyWithValueOne(characterList)

    def bruteForceApproach(self, characterList):
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """

        for i in range(len(characterList)):
            foundDuplicate = False
            for j in range(len(characterList)):
                if i != j and characterList[i] == characterList[j]:
                    foundDuplicate = True

            if not foundDuplicate:
                return characterList[i]

        return -1

    def __createCharacterCountHashTable(self, characterList):
        for character in characterList:
            self.countsHashTable[character] = self.countsHashTable.get(
                character, 0) + 1

    def __findFirstKeyWithValueOne(self, characterList):
        for character in characterList:
            if self.countsHashTable[character] == 1:
                return character

        return -1


firstNonRepeatingCharacter = FirstNonRepeatingCharacter()
print(firstNonRepeatingCharacter.optimizedApproach(
    ["a", "b", "c", "d", "c", "a", "b"]))
