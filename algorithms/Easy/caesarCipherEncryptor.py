class CaesarCipherEncrypt:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.totalCharsInAlphabet = len(self.alphabet)

    def encrypt(self, text, key):
        encryptedTextList = []
        newKey = key % self.totalCharsInAlphabet

        for character in text:
            encryptedTextList.append(
                self.__getEncryptedCharacter(character, newKey))
        return "".join(encryptedTextList)

    def __getEncryptedCharacter(self, character, key):
        characterIndexInAlphabet = self.alphabet.index(character)
        encryptedTextIndex = characterIndexInAlphabet + key
        return self.alphabet[encryptedTextIndex % self.totalCharsInAlphabet]


caesarCipherEncrypt = CaesarCipherEncrypt()
print(caesarCipherEncrypt.encrypt("abc", 54))
