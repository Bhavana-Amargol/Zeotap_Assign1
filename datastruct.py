class ASTNode:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # "operator" or "operand"
        self.left = left  # left child node (None if it's a leaf)
        self.right = right  # right child node (None if it's a leaf)
        self.value = value  # value for "operand" nodes (e.g., 30, "Sales", etc.)
        
    def __repr__(self):
        return f"ASTNode({self.node_type}, {self.value})"
