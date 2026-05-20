# description: https://leetcode.com/problems/intersection-of-two-arrays-ii/description/


class Solution(object):
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        counts = {}
        for n in nums2:
            counts[n] = counts.get(n, 0) + 1

        result = []
        for i in nums1:
            if counts.get(i, 0) > 0:
                result.append(i)
                counts[i] -= 1

        return result


def main():
    solver = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    print(solver.intersect(nums1, nums2))


main()
