from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        l, r, t, d, x = 0, n - 1, 0, n - 1, 1
        while l < r and t < d:
            # top
            for i in range(l, r):
                res[t][i] = x
                x += 1
            # right
            for i in range(t, d):
                res[i][r] = x
                x += 1
            # down
            for i in range(r, l, -1):
                res[d][i] = x
                x += 1
            # left
            for i in range(d, t, -1):
                res[i][l] = x
                x += 1
            l += 1
            r -= 1
            t += 1
            d -= 1

        if l == r:
            res[l][t] = x

        return res





if __name__ == "__main__":
    nums = 0

    print(nums)
    sol = Solution()
    res = sol.generateMatrix(nums)
    print(res)