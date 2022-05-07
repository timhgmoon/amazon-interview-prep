# solution credit to user: cmeow
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        
        m = len(matrix)
        n = len(matrix[0])
        
        #these booleans will be used to check if first row/col contains a zero
        first_row_zero = False
        first_col_zero = False
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    #two if statements will be used later to populate col/rows
                    if row == 0:
                        first_row_zero = True
                    if col == 0:
                        first_col_zero = True
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        for row in range(1, m):
            for col in range(1, n):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        if first_row_zero:
            for col in range(n):
                matrix[0][col] = 0
                
        if first_col_zero:
            for row in range(m):
                matrix[row][0] = 0
