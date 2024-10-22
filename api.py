# Create Rule:
# Endpoint: /create_rule
# Method: POST
# Description: Converts a rule string into its corresponding AST and stores it in the database.
@app.route('/create_rule', methods=['POST'])
def create_rule():
    rule_string = request.json['rule']
    ast = parse_rule_to_ast(rule_string)
    save_ast_to_db(ast)
    return jsonify({'message': 'Rule created successfully'})
    
# Combine Rules:
# Endpoint: /combine_rules
# Method: POST
# Description: Combines multiple ASTs into one optimized AST.  
    @app.route('/combine_rules', methods=['POST'])
def combine_rules():
    rules = request.json['rules']  # List of rule strings
    asts = [parse_rule_to_ast(rule) for rule in rules]
    combined_ast = combine_asts(asts)
    return jsonify({'combined_ast': ast_to_json(combined_ast)})

# Evaluate Rule:
# Endpoint: /evaluate_rule
# Method: POST
# Description: Evaluates an AST rule against the provided data attributes and returns whether the user is eligible or not.
python
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    rule_ast = request.json['rule_ast']  # AST in JSON format
    user_data = request.json['data']  # User attributes like age, department, etc.
    result = evaluate_ast(rule_ast, user_data)
    return jsonify({'eligible': result})
    
# Rule Parsing (AST Generation)
# AST Creation:
import ast

def parse_rule_to_ast(rule_string):
    # Use Python's AST module to parse string into AST
    parsed_ast = ast.parse(rule_string, mode='eval')
    return convert_to_custom_ast(parsed_ast.body)

def convert_to_custom_ast(node):
    if isinstance(node, ast.BinOp):
        # Handle binary operations (AND/OR)
        left = convert_to_custom_ast(node.left)
        right = convert_to_custom_ast(node.right)
        operator = type(node.op).__name__
        return ASTNode(node_type="operator", left=left, right=right, value=operator)
    elif isinstance(node, ast.Compare):
        # Handle comparisons like age > 30
        left = node.left
        right = node.comparators[0]
        comparison = type(node.ops[0]).__name__
        return ASTNode(node_type="operand", value=f"{left.id} {comparison} {right.n}")
    return None


