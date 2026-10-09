class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if (len(nums)==0) or (nums[0]>target or nums[-1]<target):
            return [-1,-1]
        else:
            if nums[0]==target and nums[-1]==target:
                return [0,len(nums)-1]
            elif nums[0]<target and nums[-1]>target:
                left = 0
                right = len(nums) - 1
                while right-left > 1:
                    mid = (right+left) // 2
                    if nums[mid] < target:
                        left = mid
                    else:
                        right = mid
                if nums[right] > target:
                    return [-1,-1]
                else:
                    lPos = right
                left = 0
                right = len(nums) - 1
                while right-left > 1:
                    mid = (right+left) // 2
                    if nums[mid] <= target:
                        left = mid
                    else:
                        right = mid
                rPos = left
                return [lPos,rPos]
            elif nums[0]==target and nums[-1]>target:
                left = 0
                right = len(nums) - 1
                while right-left > 1:
                    mid = (right+left) // 2
                    if nums[mid] <= target:
                        left = mid
                    else:
                        right = mid
                return [0,left]
            else:
                left = 0
                right = len(nums) - 1
                while right-left > 1:
                    mid = (right+left) // 2
                    if nums[mid] < target:
                        left = mid
                    else:
                        right = mid
                rPos = left
                return [right,len(nums)-1]


                
                
        