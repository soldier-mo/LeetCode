#description: https://leetcode.com/problems/merge-sorted-array/description/
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sortedList = sorted( nums1[:m] + nums2[:n])
        for i in range(len(sortedList)):
            nums1[i] = sortedList[i]

def main():
    solver = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solver.merge(nums1, m, nums2, n)
    print(nums1)
main()