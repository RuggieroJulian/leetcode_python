from collections import defaultdict


def bfs(nodes, level, dic):
    total_sum = 0
    children = []
    for node in nodes:
        total_sum += node.val
        if node.left: children.append(node.left)
        if node.right: children.append(node.right)
    dic[level] = total_sum
    if children:
        self.bfs(children, level + 1, dic)

d = defaultdict(int) # stores sum of each level
bfs([[1,7,0,7,-8,None,None]], 1, d)
print(max(d, key = d.get))