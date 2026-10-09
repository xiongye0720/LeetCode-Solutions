class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            left = 0
            right = len(nums) - 1
            
            # Maintain nums[left] < target <= nums[right].
            while right-left > 1:
                mid = (left+right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid

            # Adjacent bounds make right the first index with nums[right] >= target.
            return right

        