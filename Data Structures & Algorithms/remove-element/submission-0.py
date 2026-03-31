class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        # Loop through nums
        for i in range(len(nums)):
            # If the number is not the value to move/ignore
            if nums[i] != val:
                # Put it to the front of array, found using k because k elements is all we need to return
                nums[k] = nums[i]
                k += 1
        return k