#description: https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


def main():
    s = Solution()
    print(s.isPalindrome(12332))
main()