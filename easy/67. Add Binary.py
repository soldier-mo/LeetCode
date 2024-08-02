class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_asInt = int(a, 2)
        b_asInt = int(b, 2)
        
        a_b = a_asInt + b_asInt
        
        a_b_asBinary = bin(a_b)[2:]

        return a_b_asBinary
    
def main():
    a = "11"
    b = "1"
    solver = Solution()
    print(solver.addBinary(a, b))
main()
