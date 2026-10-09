class Solution:
    def search(self, nums: List[int], target: int) -> int:
        posStart = None
        posEnd = None

        if nums[-1] < nums[0]:
            left = 0
            right = len(nums) - 1
            while right-left > 1:
                mid = (left+right) // 2
                if nums[mid] >= nums[0]:
                    left = mid
                else:
                    right = mid
            if nums[0]<=target and nums[left]>=target:
                posStart = 0
                posEnd = left
            elif nums[right]<=target and nums[-1]>=target:
                posStart = right
                posEnd = len(nums) - 1
            else:
                return -1
        else:
            if target>=nums[0] and target<=nums[-1]:
                posStart = 0
                posEnd = len(nums) - 1
            else:
                return -1
        
        if nums[posEnd]>target:
            left = posStart
            right = posEnd
            while right-left > 1:
                mid = (left+right) // 2
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid
            if nums[left] == target:
                return left
            else:
                return -1
        else:
            return posEnd

        