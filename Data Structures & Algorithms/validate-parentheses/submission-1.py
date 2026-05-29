class Solution:
    def isValid(self, s: str) -> bool:
        closingTagMap = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        stack = []
        for char in s:
            if char not in closingTagMap:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if closingTagMap[char] != top:
                    return False

        return len(stack) == 0