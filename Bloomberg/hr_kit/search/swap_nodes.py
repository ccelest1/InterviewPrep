"""
assuming tree with root, nodes having left and right nodes

def inOrder_dfs(self):
    nodes = []
    if not self.root:
        return nodes
    current = self.root

    def inOrderTraverse(node):
        if not nhouode:
            return nodes

        if node.left: inOrderTraverse(node.left)
        nodes.push(node)
        if node.right: inOrderTraverse(node.right)

    inOrderTraverse(current)
    return nodes

"""
