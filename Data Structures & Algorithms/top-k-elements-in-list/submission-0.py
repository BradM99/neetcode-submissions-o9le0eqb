class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, amount in count.items():
            freq[amount].append(num)

        ret = []
        # Loop the list, starting from the highest
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                ret.append(num)
            if len(ret) == k:
                return ret