class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        loc = position
        loc.sort()

        left = 0
        right = loc[-1] -loc[0] + 1

        while right-left > 1:
            mid = (left+right) // 2
            i = 0
            isOk = True
            for j in range(m-1):
                temI = i
                while temI < len(loc):
                    if loc[temI]-loc[i] >= mid:
                        break
                    temI = temI + 1
                if temI == len(loc):
                    isOk = False
                    break
                i = temI
            if isOk:
                left = mid
            else:
                right = mid

        return left