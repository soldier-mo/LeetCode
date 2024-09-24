#Description: https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp = sorted(nums1[:m] + nums2[:n])
        for i in range(len(temp)):
            nums1[i] = temp[i]
        


def main():
    # nums1 = [2,5,6]
    # nums2 = [1,2,3,0,0,0]
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]

    m = 3
    n = 3

    s = Solution()
    s.merge(nums1, m, nums2, n)
    print(nums1)
main()