class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def calcCoord(nums):
            dx = (n-1) - (nums-1)//n
            if ((nums-1)//n)%2 == 0:
                dy = (nums-1) % n
            else:
                dy = (n-1) - (nums-1)%n
            return (dx,dy)

        n = len(board)
        ops = deque()
        ops.append(1)
        visited = {1}
        cnt = 0

        while len(ops) > 0:
            temOps = deque()
            cnt = cnt + 1
            while len(ops) > 0:
                temNode = ops.popleft()
                for item in range(temNode+1,min(temNode+6,n*n)+1):
                    temCoord = calcCoord(item)
                    if board[temCoord[0]][temCoord[1]]==-1 and (item not in visited):
                        temOps.append(item)
                        visited.add(item)
                    elif board[temCoord[0]][temCoord[1]] > 0:
                        if board[temCoord[0]][temCoord[1]] not in visited:
                            visited.add(board[temCoord[0]][temCoord[1]])
                            temOps.append(board[temCoord[0]][temCoord[1]])

            if n*n in visited:
                return cnt
            ops = temOps

        return -1