class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        preSum = nums[0]
        minPre = nums[0]
        maxSum = nums[0]

        for i in range(1,len(nums)):
            preSum = preSum + nums[i]
            # Check subarrays starting at index 0 or after the smallest earlier prefix.
            maxSum = max(preSum,preSum-minPre,maxSum)
            # Update afterward to exclude empty subarrays.
            minPre = min(minPre,preSum)

        return maxSum