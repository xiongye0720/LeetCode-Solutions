class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if startGene == endGene:
            return 0
        elif endGene not in bank:
            return -1
        else:
            bank.add(startGene)
            pattern = {}
            for item in bank:
                for i in range(8):
                    newStr = item[0:i] + '*' + item[i+1:8]
                    if newStr not in pattern:
                        pattern[newStr] = [item]
                    else:
                        pattern[newStr].append(item)

            ops = deque()
            ops.append(startGene)
            cnt = 0
            visited = {startGene}

            while len(ops) > 0:
                temOps = deque()
                cnt = cnt + 1
                while len(ops) > 0:
                    temNode = ops.popleft()
                    for i in range(8):
                        newStr = temNode[0:i] + '*' + temNode[i+1:8]
                        for item in pattern[newStr]:
                            if item!=temNode and (item not in visited):
                                visited.add(item)
                                temOps.append(item)
                        pattern[newStr] = []
                if endGene in visited:
                    return cnt
                else:
                    ops = temOps
            
            return -1