#description: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {} # Dictionary to store the last seen index of each character
        start = 0
        result = 0

        for index, value in enumerate(s):
            if value in d and d[value] >= start:
                start = d[value] + 1
            d[value] = index
            result = max(result, index - start + 1)
        return result

                    
        

def main():
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"
    s = Solution()

    print(s.lengthOfLongestSubstring(s1))
    print(s.lengthOfLongestSubstring(s2))
    print(s.lengthOfLongestSubstring(s3))
main()
