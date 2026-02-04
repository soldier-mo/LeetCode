# description: https://leetcode.com/problems/contains-duplicate-ii/description/


from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}

        for i, num in enumerate(nums):
            if num in index_map:
                # Check if the previous occurrence is within k positions
                prev_index = index_map[num]
                if abs(i - prev_index) <= k:
                    return True

            index_map[num] = i

        return False


def main():
    solver = Solution()
    n = [1, 2, 3, 1]

    print(solver.containsNearbyDuplicate(n, 3))


main()
