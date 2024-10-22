# Bonus Features
# Error Handling for Invalid Rules
# Objective: Implement error handling for incorrect rule strings (syntax errors, invalid operators, etc.) and data formats.

def test_invalid_rule_handling():
    # Invalid Rule: Missing comparison operator
    invalid_rule = "age 30 AND department = 'Sales'"
    
    try:
        parse_rule_to_ast(invalid_rule)
        assert False  # This line should not be reached
    except SyntaxError:
        assert True  # Expected error

def test_invalid_data_format_handling():
    # Invalid user data format (missing required keys)
    rule_ast = parse_rule_to_ast("age > 30 AND department = 'Sales'")
    invalid_data = {"age": 35}  # Missing department
    
    try:
        evaluate_ast(rule_ast, invalid_data)
        assert False  # Should raise a KeyError
    except KeyError:
        assert True  # Expected error

# Attribute Catalog Validation
# Objective: Ensure that attributes like age, department, salary, etc., are part of a predefined catalog. Invalid attributes should raise an error.
# Predefined attribute catalog
ATTRIBUTE_CATALOG = ["age", "department", "salary", "experience"]

def validate_rule(rule_string):
    for attribute in ATTRIBUTE_CATALOG:
        if attribute not in rule_string:
            raise ValueError(f"Invalid attribute: {attribute}")

def test_attribute_validation():
    valid_rule = "age > 30 AND department = 'Sales'"
    invalid_rule = "height > 170 AND department = 'Sales'"
    
    try:
        validate_rule(valid_rule)  # Should pass
        assert True
    except ValueError:
        assert False  # Should not raise an error
    
    try:
        validate_rule(invalid_rule)  # Should fail
        assert False  # Should raise an error
    except ValueError:
        assert True  # Expected error
        
# Rule Modification Functionality
# Objective: Allow modification of existing rules to change 
# operators, operand values, or add/remove sub-expressions.

def modify_ast(ast_node, modification_type, **kwargs):
    if modification_type == "change_operator":
        ast_node.value = kwargs.get("new_operator")
    elif modification_type == "change_operand_value":
        ast_node.value = kwargs.get("new_value")
    elif modification_type == "add_subexpression":
        new_sub_ast = kwargs.get("new_sub_ast")
        ast_node.right = new_sub_ast  # Add new subexpression to the right
    
def test_rule_modification():
    # Original Rule: age > 30 AND department = 'Sales'
    rule_ast = parse_rule_to_ast("age > 30 AND department = 'Sales'")
    
    # Modify the operator from AND to OR
    modify_ast(rule_ast, "change_operator", new_operator="OR")
    assert rule_ast.value == "OR"
    
    # Change operand value for age
    modify_ast(rule_ast.left, "change_operand_value", new_value="age < 40")
    assert rule_ast.left.value == "age < 40"
    
    # Add a sub-expression for salary
    new_sub_ast = parse_rule_to_ast("salary > 50000")
    modify_ast(rule_ast, "add_subexpression", new_sub_ast=new_sub_ast)
    assert rule_ast.right.value == "salary > 50000"
