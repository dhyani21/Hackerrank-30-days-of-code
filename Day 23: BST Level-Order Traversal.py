'''

Task:
A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to right, top to bottom. 
You are given a pointer, root, pointing to the root of a binary search tree. Complete the levelOrder function provided in your editor so that it prints the
level-order traversal of the binary search tree.

Hint: You'll find a queue helpful in completing this challenge.

Function Description:
Complete the levelOrder function in the editor below.

levelOrder has the following parameter:
- Node pointer root: a reference to the root of the tree

Prints
- Print node.data items as space-separated line of integers. No return value is expected.

'''

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
        
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        q = [ root ]
        for current in q:    
            if current:
                print(current.data, end=' ')

                q.append(current.left)
                q.append(current.right) 

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
