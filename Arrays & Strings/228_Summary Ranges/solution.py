class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        left = 0
        while left < len(nums):
            right = left + 1
            # Extend the range until a gap is found.
            while right < len(nums):
                if nums[right]-nums[right-1] > 1:
                    break
                right = right + 1
            # The current range covers indices [left, right).
            if right == left + 1:
                res.append(str(nums[right-1]))
            else:
                temStr = str(nums[left]) + '->' + str(nums[right-1])
                res.append(temStr)
            # Start the next range at the first unprocessed element.
            left = right
        
        return res