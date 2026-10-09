class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] > nums[-1]:
            left = 0
            right = len(nums) - 1
            while right-left > 1:
                mid = (left+right) // 2
                if nums[mid] >= nums[0]:
                    left = mid
                else:
                    right = mid
            return nums[right]
        else:
            return nums[0]
        