class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftIdx = 0
        rightIdx = len(s) - 1

        while leftIdx < rightIdx:
            if leftIdx < rightIdx and not self.alphaNum(s[leftIdx]):
                leftIdx += 1
                continue
            if rightIdx > leftIdx and not self.alphaNum(s[rightIdx]):
                rightIdx -= 1
                continue
            if s[leftIdx].lower() != s[rightIdx].lower():
                return False
            leftIdx += 1
            rightIdx -= 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))