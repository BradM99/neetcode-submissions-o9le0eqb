class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newStr = []
        len1 = len(word1)
        len2 = len(word2)

        left = right = 0

        while left < len1 or right < len2:
            if left < len1:
                newStr.append(word1[left])
                left += 1
            
            if right < len2:
                newStr.append(word2[right])
                right += 1
        
        return "".join(newStr)
