# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        result=[]
        queue=deque([root])

        while queue:
            level=[]
            level_size=len(queue)


            for _ in range(level_size):
                Node=queue.popleft()
                level.append(Node.val)

                if Node.left:
                    queue.append(Node.left)
                
                if Node.right:
                    queue.append(Node.right)

            result.append(level)
        return result
            
        