# description: https://leetcode.com/problems/valid-palindrome/description/

from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString = [x.lower() for x in s if x.isalnum()]
        return cleanString == cleanString[::-1]

def main():
    solver = Solution()
    s = "A man, a plan, a canal: Panama"
    s1 = "race a car"

    print(solver.isPalindrome(s))
    print(solver.isPalindrome(s1))

main()
