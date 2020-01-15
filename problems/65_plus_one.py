from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1

        while idx >= 0:
            if digits[idx] == 9:
                digits[idx] = 0
                idx -= 1
            else:
                digits[idx] += 1
                return digits

        digits.insert(0, 1)

        return digits

if __name__ == "__main__":

    nums = [9]
    sol = Solution()
    res = sol.plusOne(nums)
    print(res)