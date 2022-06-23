# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # left, node, right
        list = []
        if root == None:
            return list
        if root.left != None:
            list.extend(self.inorderTraversal(root.left))
        list.append(root.val)
        if root.right != None:
            list.extend(self.inorderTraversal(root.right))
        return list

def buildBinaryTree(arr, node, i, n):
    if i < n and arr[i] != None:
        node = TreeNode(val=arr[i])
        node.left = buildBinaryTree(arr, node.left,  i + 1, n)
        node.right = buildBinaryTree(arr, node.right,  i + 2, n)
    return node

input = [1,None,2,3]

root = None
root = buildBinaryTree(input, root, 0, len(input))

sol = Solution()
print(sol.inorderTraversal(root))