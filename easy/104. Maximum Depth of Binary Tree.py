#description: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        return max(leftDepth, rightDepth) + 1
    

###################################
#               main              #
###################################

def main():
    # Create a binary tree
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    #
    # The maximum depth of this tree is 3.

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    max_depth = solution.maxDepth(root)

    print(max_depth)

main()