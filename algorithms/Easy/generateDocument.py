class GenerateDocument:
    """
    Time Complexity: O(n+m)
    Space Complexity: O(c)

    n = No. of characters in document
    m = No. of characters in characters
    c = No. of unique characters in characters
    """

    def __init__(self):
        self.hashTable = {}

    def canGenerateDocument(self, characters, document):
        self.__generateCharacterHashTable(characters)
        return self.__isDocumentSubsetOfCharacter(document)

    def __generateCharacterHashTable(self, characters):
        for char in characters:
            if not self.__isCharacterInHashTable(char):
                self.hashTable[char] = 0

            self.hashTable[char] += 1

    def __isDocumentSubsetOfCharacter(self, document):
        for char in document:
            if not self.__isCharacterInHashTable(char) or self.hashTable[char] == 0:
                return False

            self.hashTable[char] -= 1
        return True

    def __isCharacterInHashTable(self, character):
        return character in self.hashTable


document = "AlgoExpert is the Best!"
characters = "BSte!hetsi ogEAXpelrt x "
generateDocument = GenerateDocument()
print(generateDocument.canGenerateDocument(characters, document))
