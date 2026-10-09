class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        if matrix[0][0]<=target and matrix[m-1][n-1]>target:
            left = 0
            right = m*n - 1
            while right-left > 1:
                mid = (left+right) // 2
                row = mid // n
                col = mid % n
                if matrix[row][col] <= target:
                    left = mid
                else:
                    right = mid
            if matrix[left//n][left%n] == target:
                return True
            else:
                return False
        elif matrix[0][0]>target and matrix[m-1][n-1]>target:
            return False
        elif matrix[0][0]<=target and matrix[m-1][n-1]<=target:
            if matrix[m-1][n-1] == target:
                return True
            else:
                return False
        