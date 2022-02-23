# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node): # BFS
        if not node:
            return node
        nodeCopy = Node(node.val, [])
        dic = {node : nodeCopy}
        queue = [node]
        while queue:
            node = queue.pop(0)
            for x in node.neighbors:
                if x not in dic: # not visited
                    copy = Node(x.val, [])
                    dic[x] = copy
                    dic[node].neighbors.append(copy)
                    queue.append(x)
                else:
                    dic[node].neighbors.append(dic[x])
        return nodeCopy

class Solution:
    def cloneGraph(self, node): # DFS iteratively
        if not node:
            return node
        nodeCopy = Node(node.val, [])
        dic = {node : nodeCopy}
        stack = [node]
        while stack:
            node = stack.pop()
            for x in node.neighbors:
                if x not in dic:
                    copy = Node(x.val, [])
                    dic[x] = copy
                    dic[node].neighbors.append(copy)
                    stack.append(x)
                else:
                    dic[node].neighbors.append(dic[x])
        return nodeCopy

class Solution:
    def cloneGraph(self, node): # DFS recursively
        if not node:
            return node
        nodeCopy = Node(node.val, [])
        dic = {node : nodeCopy}
        self.dfs(node, dic)
        return nodeCopy
    def dfs(self, node, dic):
        for x in node.neighbors:
            if x not in dic:
                copy = Node(x.val, [])
                dic[x] = copy
                dic[node].neighbors.append(copy)
                self.dfs(x, dic)
            else:
                dic[node].neighbors.append(dic[x])
