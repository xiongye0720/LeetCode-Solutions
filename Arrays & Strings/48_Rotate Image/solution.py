class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        maxLvl = (n+1) // 2
        lvl = 0
        left = 0
        right = n - 1
        while lvl < maxLvl:
            for i in range(right-left):
                temNode = matrix[left+i][right]
                matrix[left+i][right] = matrix[left][left+i]
                matrix[left][left+i] = temNode

                temNode = matrix[right][right-i]
                matrix[right][right-i] = matrix[left][left+i]
                matrix[left][left+i] = temNode

                temNode = matrix[right-i][left]
                matrix[right-i][left] = matrix[left][left+i]
                matrix[left][left+i] = temNode
            
            lvl = lvl + 1
            left = left + 1
            right = right - 1