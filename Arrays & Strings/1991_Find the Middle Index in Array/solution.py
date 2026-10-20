class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        vals = nums
        # preSum[i] stores the sum of the first i elements.
        preSum = [0] * (len(vals)+1)
        for i in range(len(vals)):
            preSum[i+1] = preSum[i] + vals[i]

        left = 0
        isFound = False
        res = []

        while left < len(vals):
            # Both sums exclude the current element.
            leftSum = preSum[left]
            rightSum = preSum[len(vals)] - preSum[left+1]

            if rightSum > leftSum:
                left = left + 1
            else:
                if rightSum == leftSum:
                    # Stop at the leftmost valid index.
                    isFound = True
                    res.append(left)
                    break
                else:
                    left = left + 1

        if isFound:
            return res[0]
        else:
            return -1