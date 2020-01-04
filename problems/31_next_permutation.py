from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i < 0:
            nums.sort()
            return
        print(i)
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        print(j)
        nums[i], nums[j] = nums[j], nums[i]
        low, high = i + 1, len(nums) - 1
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1
        # #may not be "inplace"
        # right = nums[i + 1:]
        # right.sort()
        # nums[i + 1:] = right


if __name__ == "__main__":
    nums = [1, 3, 2]
    print(nums)
    sol = Solution()
    sol.nextPermutation(nums)
    print(nums)
