# description: https://leetcode.com/problems/intersection-of-two-arrays/description/


class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

        return list(set(nums1).intersection(nums2))


def main():
    solver = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    print(solver.intersection(nums1, nums2))


main()
