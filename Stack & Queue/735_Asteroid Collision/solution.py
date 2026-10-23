class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        nums = asteroids

        stack = []
        ans = []

        for item in nums:
            if item > 0:
                stack.append(item)
            else:
                stack.append(item)

                while stack != [] and stack[-1] < 0:
                    temNeg = stack.pop()
                    if stack == []:
                        ans.append(temNeg)
                        continue
                    else:
                        temPos = stack.pop()
                        if temPos + temNeg == 0:
                            continue
                        else:
                            if temPos > -temNeg:
                                stack.append(temPos)
                            else:
                                stack.append(temNeg)

        return ans + stack