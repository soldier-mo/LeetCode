#not my solution src = https://leetcode.com/problems/longest-common-prefix/solutions/3273176/python3-c-java-19-ms-beats-99-91/
#description: https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans=""
        v = sorted(strs)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if(first[i]!=last[i]): 
                return ans
            ans += first[i]
        return ans

def main():
    s = ["flower","flow","loght"]
    solver = Solution()
    print(solver.longestCommonPrefix(s))
    print(sorted( ["dog","racecar","car"]))
    print(sorted(["flower","flow","loght"]))
main()
