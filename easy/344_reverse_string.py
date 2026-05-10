# description: https://leetcode.com/problems/reverse-string/description/


class Solution(object):
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s


def main():
    solver = Solution()
    s = ["1", "2", "3", "4"]

    print(solver.reverseString(s))


main()
