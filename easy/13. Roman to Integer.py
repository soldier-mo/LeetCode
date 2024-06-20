
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        RomanInt = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        i = 0
        while i < len(s)-1:
            print(result ,i)
            if RomanInt[s[i]] < RomanInt[s[i+1]]:
                print("j")
                result += RomanInt[s[i+1]]-RomanInt[s[i]]
                i += 2
                continue
            result += RomanInt[s[i]]
            i+=1
        if i < len(s):
            result += RomanInt[s[i]]
        return result

def main():
    s = "MCMXCIV"
    solver = Solution()
    print(solver.romanToInt(s))
main()

# what is better copilot or chatgpt
