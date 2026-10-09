class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        proj = {}
        caps = []
        for i in range(len(profits)):
            if capital[i] in proj:
                proj[capital[i]].append(profits[i])
            else:
                proj[capital[i]] = [profits[i]]
                caps.append(capital[i])
        caps.sort()

        ops = []
        ptr = 0
        while k > 0:
            while ptr < len(caps):
                if caps[ptr] > w:
                    break
                for item in proj[caps[ptr]]:
                    heapq.heappush(ops,-1*item)
                ptr = ptr + 1
            if len(ops) == 0:
                break
            w = w + (-1 * heapq.heappop(ops))
            k = k - 1
        
        return w






        