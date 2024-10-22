
from flask import Flask, request, jsonify
import ast

app = Flask(__name__)


class ASTNode:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type
        self.left = left
        self.right = right
        self.value = value

# Function to parse rule into AST
def parse_rule_to_ast(rule_string):
    parsed_ast = ast.parse(rule_string, mode='eval')
    return convert_to_custom_ast(parsed_ast.body)

def convert_to_custom_ast(node):
    if isinstance(node, ast.BinOp):
        left = convert_to_custom_ast(node.left)
        right = convert_to_custom_ast(node.right)
        operator = type(node.op).__name__
        return ASTNode(node_type="operator", left=left, right=right, value=operator)
    elif isinstance(node, ast.Compare):
        left = node.left
        right = node.comparators[0]
        comparison = type(node.ops[0]).__name__
        return ASTNode(node_type="operand", value=f"{left.id} {comparison} {right.n}")
    return None

# API Endpoint to create a rule
@app.route('/create_rule', methods=['POST'])
def create_rule():
    rule_string = request.json['rule']
    ast = parse_rule_to_ast(rule_string)
    # You would save ast to database here
    return jsonify({'message': 'Rule created successfully', 'ast': repr(ast)})

# API Endpoint to evaluate rule against user data
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    rule_ast = request.json['rule_ast']
    user_data = request.json['data']
    result = evaluate_ast(rule_ast, user_data)
    return jsonify({'eligible': result})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
