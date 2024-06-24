#description: https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets = []
        bracketsMap = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        if len(s) % 2 != 0:
            return False

        for i in range(len(s)):
            if s[i] in bracketsMap.values():
                openBrackets.append(s[i])
            # it's a closing bracket, there are open brackets, and it matches with the last opened
            elif s[i] in bracketsMap and openBrackets and bracketsMap[s[i]] == openBrackets[-1]:
                openBrackets.pop()
            else:
                return False
        return not openBrackets

def main():
    s = "[([]])"
    solver = Solution()
    print(solver.isValid(s))
    print(solver.isValid("{[]}"))
main()
