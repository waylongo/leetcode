from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        res = cur = nums[0]

        for i in nums[1:]:
            cur = max(i, cur + i)
            res = max(res, cur)

        return res


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums
        res = nums[0]

        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
            res = max(res, dp[i])

        return res


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = nums[0]

        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] = nums[i - 1] + nums[i]

            res = max(res, nums[i])

        return res


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] = nums[i - 1] + nums[i]

        res = max(nums)

        return res


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]

        return max(nums)


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(nums)
    sol = Solution()
    res = sol.maxSubArray(nums)
    print(res)
