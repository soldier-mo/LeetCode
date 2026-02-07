# description: https://leetcode.com/problems/invert-binary-tree/description/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

def main():
    #       2
    #      / \
    #     1   3

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)

    solution = Solution()
    solution.invertTree(root)
    print(root.val, root.left.val, root.right.val)


main()
