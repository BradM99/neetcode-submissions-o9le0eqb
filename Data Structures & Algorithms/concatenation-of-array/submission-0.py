class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums) * 2
        i = 0
        ans = []

        while len(ans) < n:
            ans.append(nums[i])
            i += 1
            if i % len(nums) == 0:
                i = 0
        return ans