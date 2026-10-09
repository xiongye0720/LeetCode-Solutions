class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) >= 3:
            preSum = nums[0]
            minPreSum = nums[0]
            maxVal = nums[0]
            for i in range(1,len(nums)):
                preSum = preSum + nums[i]
                maxVal = max(maxVal,preSum,preSum-minPreSum)
                minPreSum = min(preSum,minPreSum)
            total = preSum
            preSum = nums[1]
            maxPreSum = nums[1]
            minVal = nums[1]
            for i in range(2,len(nums)-1):
                preSum = preSum + nums[i]
                minVal = min(minVal,preSum,preSum-maxPreSum)
                maxPreSum = max(preSum,maxPreSum)
            return max(maxVal,total-minVal)
        elif len(nums) == 2:
            return max(nums[0],nums[1],nums[0]+nums[1])
        else:
            return nums[0]