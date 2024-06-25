#description: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle) if needle in haystack else -1
        
def main():
    haystack = "sadbutsad"
    needle = "sad"
    solver = Solution()
    print(solver.strStr(haystack, needle))
main()
