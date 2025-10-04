# Approach:
# - We need to generate all anti-diagonals of the matrix.
# - An anti-diagonal starts either from the first row (col 0..N-1) 
#   or from the last column (row 1..N-1).
# - Traverse diagonally down-left (i+1, j-1) for each starting point.
# - Store values in result array at correct positions.
# - Fill unused cells with 0 by default.
#
# Time Complexity: O(N^2)  -> Every element of the matrix is processed once
# Space Complexity: O(1)   -> Constant extra space (excluding output storage)


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A)

        # Prepare result with 0s, size (2n-1) x n
        result = [[0] * n for _ in range(2 * n - 1)]
        row_index = 0

        # Anti-diagonals starting from first row
        for col in range(n):
            i, j, col_index = 0, col, 0
            while i < n and j >= 0:
                result[row_index][col_index] = A[i][j]
                i += 1
                j -= 1
                col_index += 1
            row_index += 1

        # Anti-diagonals starting from last column
        for row in range(1, n):
            i, j, col_index = row, n - 1, 0
            while i < n and j >= 0:
                result[row_index][col_index] = A[i][j]
                i += 1
                j -= 1
                col_index += 1
            row_index += 1

        return result


# Example usage:
if __name__ == "__main__":
    matrix1 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    print(Solution().diagonal(matrix1))
    # Expected:
    # [[1, 0, 0],
    #  [2, 4, 0],
    #  [3, 5, 7],
    #  [6, 8, 0],
    #  [9, 0, 0]]