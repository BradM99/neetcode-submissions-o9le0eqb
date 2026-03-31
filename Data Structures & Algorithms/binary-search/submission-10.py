class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1        
        
        # We want to keep going until the pointers meet inwards
        while left <= right:
            # Safe way to get the mid point within the bounds of L and R
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1