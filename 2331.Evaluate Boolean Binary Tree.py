# You are given the root of a full binary tree with the following properties:

# Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
# Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
# The evaluation of a node is as follows:

# If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
# Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
# Return the boolean result of evaluating the root node.

# A full binary tree is a binary tree where each node has either 0 or 2 children.

# A leaf node is a node that has zero children.

# QUESTION-LINK: https://leetcode.com/problems/evaluate-boolean-binary-tree/description/

# INTUITION: 
# * Recursion is in fact the most popularly used for this kind of questions especially when dealing with Trees. 
# * Using recursion we can reach until the leafnode.. and perform the required operation and keep updating the parent node. 
# * Then finally return the last node which has a boolean value.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root) -> bool:
        # This condition checks if the present node is the leafNode.. if then it returns the value
        if root.right == None and root.left == None:
            return root.val
        
        leftNodeVal = self.evaluateTree(root.left)  # Has the boolean value of the left node
        rightNodeVal = self.evaluateTree(root.right) # Has the boolean value of the right node
        #Or operations
        if root.val == 2:
            return leftNodeVal or rightNodeVal
        
        #And operartions
        elif root.val == 3:
            return leftNodeVal and rightNodeVal
        


# 95.73%