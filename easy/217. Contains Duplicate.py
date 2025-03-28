# description: https://leetcode.com/problems/contains-duplicate/description/


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


def main():
    solver = Solution()
    n = [1, 2, 3, 1]

    print(solver.containsDuplicate(n))


main()
