class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        bracketPairs = {
            ")" : "(",
            "]" : "[", 
            "}" : "{"
            }
        
        for b in s:
            if b in bracketPairs:
                if stack and stack[-1] == bracketPairs[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)

        if stack:
            return False
        else:
            return True