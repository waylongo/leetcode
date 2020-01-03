from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        if i < 0:
            nums.sort()
            return
        print(i)
        j = len(nums) - 1
        while j >= i and nums[j] <= nums[i]:
            j -= 1
        print(j)
        nums[i], nums[j] = nums[j], nums[i]
        right = nums[i+1:]
        right.sort()

        nums[i+1:] = right


if __name__ == "__main__":
    nums = [5, 1, 1]
    print(nums)
    sol = Solution()
    sol.nextPermutation(nums)
    print(nums)
