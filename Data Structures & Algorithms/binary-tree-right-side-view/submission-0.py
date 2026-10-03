# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []

        
        result=[]
        queue=deque([root])

        while queue:
            level=[]
            level_size=len(queue)


            for i in range(level_size):

                Node=queue.popleft()

                if (i==level_size-1):
                    result.append(Node.val)
                
                if Node.left:
                    queue.append(Node.left)

                if Node.right:
                    queue.append(Node.right)
                
        return result