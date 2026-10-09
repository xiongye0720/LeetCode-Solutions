class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        notFound = True
        total = 0
        minLen = float('inf')

        while left < len(nums):
            while right<len(nums) and notFound:
                total = total + nums[right]
                right = right + 1
                if total >= target:
                    notFound = False
                    break
            if notFound:
                break
            minLen = min(minLen,right-left)
            if minLen == 1:
                break
            total = total - nums[left]
            left = left + 1
            if total < target:
                notFound = True
        
        if minLen == float('inf'):
            return 0
        else:
            return minLen
