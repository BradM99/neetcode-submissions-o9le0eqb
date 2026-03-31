class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)

        for word in strs:
            chars = [0] * 26
            for i in range(len(word)):
                chars[ord(word[i]) - ord('a')] += 1
            key = tuple(chars)
            words[key].append(word)
            
        return list(words.values())