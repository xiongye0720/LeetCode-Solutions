class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        task = [h]
        nums = piles

        right = 0
        for item in nums:
            if item > right:
                right = item
        left = 0

        while right-left > 1:
            mid = (right+left) // 2
            temHours = 0
            isOk = True
            for item in nums:
                temHours = temHours + (item-1)//mid + 1
                if temHours > task[0]:
                    isOk = False
                    break
            if isOk:
                right = mid
            else:
                left = mid

        return right