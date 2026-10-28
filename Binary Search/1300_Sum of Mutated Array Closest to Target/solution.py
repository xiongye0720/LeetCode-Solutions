class Solution:
    def findBestValue(self, arr: list[int], target: int) -> int:
        targetInfo = [target]
        nums = arr

        total = 0
        maxVal = 0
        for item in nums:
            total = total + item
            maxVal = max(maxVal,item)

        if total <= targetInfo[0]:
            return maxVal
        else:
            left = 0
            right = maxVal
            while right-left != 1:
                mid = (left+right)//2
                temSum = 0
                for item in nums:
                    if item <= mid:
                        temSum = temSum + item
                    else:
                        temSum = temSum + mid
                if temSum > targetInfo[0]:
                    right = mid
                else:
                    left = mid

            lowTotal = 0
            highTotal = 0
            for item in nums:
                if item <= left:
                    lowTotal = lowTotal + item
                else:
                    lowTotal = lowTotal + left

                if item <= right:
                    highTotal = highTotal + item
                else:
                    highTotal = highTotal + right

            if abs(lowTotal-targetInfo[0]) <= abs(highTotal-targetInfo[0]):
                return left
            else:
                return right