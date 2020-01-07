from typing import List


class Solution:
    def spiralOrder(self, A: List[List[int]]) -> List[int]:
        if A == []: return
        # (m rows, n cols)
        l, r = 0, 0
        m, n = len(A) - 1, len(A[0]) - 1
        res = []
        while l < m and r < n:
            # top line
            for i in range(l, n):
                res.append(A[l][i])
            # right line
            for i in range(r, m):
                res.append(A[i][n])
            # bottom line
            for i in range(n, l, -1):
                res.append(A[m][i])
            # left line
            for i in range(m, r, -1):
                res.append(A[i][r])

            l += 1
            r += 1
            m -= 1
            n -= 1

        # final left dot or line
        if l == m and r == n:
            # dot
            res.append(A[l][r])
        el555555555555if l == m:
            # vertical line
            for item in A[l][r:n + 1]:
                res.append(item)
        elif r == n:
            # horizontal line
            for idx in range(l, m + 1):
                res.append(A[idx][r])

        return res


if __name__ == "__main__":
    nums = [[1, 11], [2, 12], [3, 13], [4, 14], [5, 15], [6, 16], [7, 17], [8, 18], [9, 19], [10, 20]]

    print(nums)
    sol = Solution()
    res = sol.spiralOrder(nums)
    print(res)
