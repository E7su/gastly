# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def helper(left, right):

            if left > right:
                # Base case: ( also known as stop condtion )
                return None

            else:
                # General case:
                # Solve by divide-and-conquer

                # conquer
                mid = left + (right - left) // 2
                root = TreeNode(nums[mid])

                # divide
                root.left = helper(left, mid-1)
                root.right = helper(mid+1, right)

                return root

        # ----------------------
        return helper(0, len(nums)-1)
