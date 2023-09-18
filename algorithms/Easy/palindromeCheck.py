class PalindromeCheck:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def check(self, element):
        startIndex = 0
        endIndex = len(element)-1

        while startIndex < endIndex:
            if element[startIndex] != element[endIndex]:
                return False
            startIndex += 1
            endIndex -= 1
        return True


palindromeCheck = PalindromeCheck()
print(palindromeCheck.check("abcdcba"))
