class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        score = nums

        ops = deque()
        ops.append(0)
        maxScore = [score[0]] * n

        for i in range(1,n):
            maxScore[i] = maxScore[ops[0]] + score[i]
            while len(ops) > 0:
                if maxScore[ops[-1]] > maxScore[i]:
                    break
                ops.pop()
            ops.append(i)
            if ops[0] < i-k+1:
                ops.popleft()

        return maxScore[-1]