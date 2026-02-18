# description: https://leetcode.com/problems/valid-anagram/description/


class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)


def main():
    solver = Solution()
    s = "aana"
    t = "anaa"
    print(solver.isAnagram(s, t))

    s = "rat"
    t = "car"
    print(solver.isAnagram(s, t))


main()
