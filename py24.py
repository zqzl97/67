-*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        res = []
        if not root:
            return res
        self.target = expectNumber
        self.dfs(root, res, [root.val])
        res = self.change(res)
        return res

    def dfs(self, root, res, path):
        if not root.left and not root.right and sum(path) == self.target:
            res.append(path)
        if root.left:
            self.dfs(root.left, res, path + [root.left.val])
        if root.right:
            self.dfs(root.right, res, path + [root.right.val])
    def change(self, x):
        for i in range(len(x)):
            for j in range(len(x)):
                if len(x[i]) > len(x[j]):
                    x[i], x[j] = x[j], x[i]
        return x
 
 
 # leetcode 112.路径总和 I
 class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # corner case
        if root == None:
            return False
        # 递归出口 判断是否为叶子节点
        if root.left == None and root.right == None:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
 
 
 
 #leetcode 113. 路径总和 II
 class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        self.dfs(root, res, [root.val], sum)
        return res
    def dfs(self, root, res, path, sum):
        sum -= root.val
        if not root.left and not root.right and sum == 0:
            res.append(path)
        if root.left:
            self.dfs(root.left, res, path + [root.left.val], sum)
        if root.right:
            self.dfs(root.right, res, path + [root.right.val], sum)
 
 
 
 #leetcode 437. 路径总和 III
 class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None:
            return 0
        def dfs(root, sum):
            if root == None:
                return 0
            sum -= root.val
            count = 1 if sum == 0 else 0
            # 从当前节点开始总共有几条符合条件的路径
            return count + dfs(root.left, sum) + dfs(root.right, sum)
            # 因为不需要从根结点开始所以最后统计的是root+left+right的总和
        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
