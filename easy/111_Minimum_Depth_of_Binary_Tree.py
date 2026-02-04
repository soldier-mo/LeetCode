# Description: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        #if one node do not exist return depth of other one
        if not root.left or not root.right:
            return max(left, right) + 1
        
        return min(left, right) + 1
    
###################################
#               main              #
###################################

def main():
    def new_node(val):
        return TreeNode(val)

    root1 = new_node(3)
    root1.left = new_node(9)
    root1.right = new_node(20)
    root1.right.left = new_node(15)
    root1.right.right = new_node(7)

    solution = Solution()

    print(solution.minDepth(root1))  # Expected output: 2

main()