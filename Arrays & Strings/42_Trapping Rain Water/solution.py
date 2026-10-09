class Solution:
    def trap(self, height: List[int]) -> int:
        cntr = deque()
        cntr.append(-1)
        count = 0
        for item in height:
            if item >= cntr[0]:
                if len(cntr) == 1:
                    cntr.popleft()
                    cntr.append(item)
                else:
                    temHt = cntr.popleft()
                    while len(cntr) > 0:
                        count = count + (temHt - cntr.popleft())
                    cntr.append(item)
            else:
                cntr.append(item)
        
        while len(cntr) > 1:
            temHt = cntr.pop()
            if cntr[-1] >= temHt:
                continue
            else:
                while cntr[-1] < temHt:
                    count = count + (temHt - cntr.pop())

        return count
