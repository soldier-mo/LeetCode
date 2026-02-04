#description: https://leetcode.com/problems/length-of-last-word/description/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastWord = ""
        wordStarted = False
        s = s[::-1]
        for i in range(len(s)):
            if wordStarted and s[i] == " ":
                return len(lastWord)
            if s[i].isalpha():
                wordStarted = True
                lastWord += s[i]
        return len(lastWord)

def main():
    word = "Helllllll World"
    solver = Solution()
    print(solver.lengthOfLastWord(word))
main()
