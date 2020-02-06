from typing import List


class Solution:
    def searchMatrix(self, A, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not A:
            return False
        m, n = len(A), len(A[0])
        row, col = m - 1, 0

        while row >= 0 and col < n:
            if A[row][col] == target:
                return True
            elif A[row][col] < target:
                col += 1
            elif A[row][col] > target:
                row -= 1

        return False

if __name__ == "__main__":

    matrix = \
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]

    #matrix = []
    sol = Solution()
    res = sol.searchMatrix(matrix, 20)
    print(res)