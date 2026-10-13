class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        info = [limit]
        nums = people

        high = []
        low = []
        threshold = (info[0]//2) + 1
        for item in nums:
            if item >= threshold:
                high.append(item)
            else:
                low.append(item)
        high.sort(reverse=True)
        high = deque(high)
        low.sort()
        low = deque(low)

        cnt = 0
        while len(high)>0 and len(low)>0:
            temHigh = high.popleft()
            cnt = cnt + 1
            if temHigh+low[0] <= info[0]:
                low.popleft()

        if len(high) > 0:
            cnt = cnt + len(high)
        if len(low) > 0:
            cnt = cnt + (len(low)+1)//2

        return cnt