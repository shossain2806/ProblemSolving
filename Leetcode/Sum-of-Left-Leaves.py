# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left = root.left
        sum = left.val if left != None and (left.left == None and left.right == None) else 0
        sum = sum + self.sumOfLeftLeaves(root.left)
        sum = sum + self.sumOfLeftLeaves(root.right)
        
        return sum
        

# complete binary tree
def buildBinaryTree(arr, node, i, n):
    if i < n and arr[i] != None:
        node = TreeNode(val=arr[i])
        node.left = buildBinaryTree(arr, node.left, 2 * i + 1, n)
        node.right = buildBinaryTree(arr, node.right, 2 * i + 2, n)
    return node

input = [3,9,20,None, None ,15,7]

lenght = len(input)
root = None
root = buildBinaryTree(input, root, 0, lenght)


sol = Solution()
print(sol.sumOfLeftLeaves(root))