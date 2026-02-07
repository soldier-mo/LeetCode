# description:https://leetcode.com/problems/count-complete-tree-nodes/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        num = 1
        return num + self.countNodes(root.left) + self.countNodes(root.right)

def main():
    solver = Solution()

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(1)

    print(solver.countNodes(root))


main()
