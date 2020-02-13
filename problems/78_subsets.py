from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res += [[i] + j for j in res]

        return res


if __name__ == "__main__":

    nums = [1,2,3]
    print(nums)
    sol = Solution()
    res = sol.subsets(nums)
    print(res)