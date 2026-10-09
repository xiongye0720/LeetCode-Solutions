class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # left is the write position; right is the current group start.
        left = 0
        right = 0
        length = 1
        while right < len(nums):
            # Find the end of the current group of equal values.
            tem = right
            while tem < len(nums):
                if nums[tem] != nums[right]:
                    break
                tem = tem + 1
            
            # Keep one value from this group.
            step = min(tem-right,length)
            for i in range(step):
                nums[left+i] = nums[right+i]
            
            left = left + step
            right = tem
            
        return left