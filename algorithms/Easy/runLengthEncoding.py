class RunLengthEncoding:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def encode(self, string):
        self.chars = []
        currentRunLength = 1
        for i in range(1, len(string)):
            currentCharacter = string[i]
            previousCharacter = string[i-1]

            if currentCharacter != previousCharacter or currentRunLength == 9:
                self.chars.extend([str(currentRunLength), string[i-1]])
                currentRunLength = 0

            currentRunLength += 1

        self.chars.extend([str(currentRunLength), string[-1]])
        return "".join(self.chars)


lengthEncoding = RunLengthEncoding()
print(lengthEncoding.encode('AAAAAAAAAABBCCCDDD'))
