# description: https://leetcode.com/problems/isomorphic-strings/description/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_to_t = {}
        t_to_s = {}
        
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            
            # Check s to t mapping
            if s_char in s_to_t:
                if s_to_t[s_char] != t_char:
                    return False
            else:
                s_to_t[s_char] = t_char
                
            # Check t to s mapping
            if t_char in t_to_s:
                if t_to_s[t_char] != s_char:
                    return False
            else:
                t_to_s[t_char] = s_char
        
        return True

        


def main():
    solver = Solution()
    s = "badc"
    t = "baba"

    print(solver.isIsomorphic(s, t))


main()
