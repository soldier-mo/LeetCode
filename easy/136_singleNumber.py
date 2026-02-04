# description: https://leetcode.com/problems/single-number/description/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        # XOR all numbers in the array
        for num in nums:
            result ^= num

        return result


def main():
    solver = Solution()
    nums = [2, 2, 1]
    nums2 = [4, 1, 2, 1, 2]

    print(solver.singleNumber(nums))
    print(solver.singleNumber(nums2))


main()
