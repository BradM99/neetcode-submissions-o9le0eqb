class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        bracketPairs = { ")" : "(", "]" : "[", "}" : "{"}

        for char in s:
            if char in bracketPairs:
                if stack and stack[-1] == bracketPairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if stack:
            return False
        else:
            return True                        