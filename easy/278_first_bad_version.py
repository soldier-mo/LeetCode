# description: https://leetcode.com/problems/first-bad-version/description/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


from turtle import right


class Solution(object):
    def firstBadVersion(self, n):
        left = 0
        right = n

        while left < right:
            mid = (left + right) // 2

            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

    def isBadVersion(self, version):
        return version > 3


def main():
    solver = Solution()
    n = 5

    print(solver.firstBadVersion(n))


main()