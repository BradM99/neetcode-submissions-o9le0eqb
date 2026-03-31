class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        small, large = 0, len(nums)-1

        while small <= large:
            mid = (small + large) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                large = mid-1
            elif target > nums[mid]:
                small = mid+1
        return -1
