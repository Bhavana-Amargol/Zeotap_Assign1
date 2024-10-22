 # Test Case 1: Create Individual Rules and Verify AST Representation
# Objective: Ensure that individual rules are correctly parsed into AST format.
# Input: Rule strings (e.g., "age > 30 AND department = 'Sales'")
# Expected Output: Correct AST structure corresponding to the rule.

def test_create_rule():
    # Rule 1
    rule1 = "age > 30 AND department = 'Sales'"
    ast = parse_rule_to_ast(rule1)
    
    # Expected AST Structure
    assert ast.node_type == "operator"
    assert ast.value == "AND"
    assert ast.left.node_type == "operand"
    assert ast.left.value == "age > 30"
    assert ast.right.node_type == "operand"
    assert ast.right.value == "department == 'Sales'"

    # Rule 2
    rule2 = "age < 25 AND department = 'Marketing'"
    ast2 = parse_rule_to_ast(rule2)
    
    # Expected AST Structure
    assert ast2.node_type == "operator"
    assert ast2.left.value == "age < 25"
    assert ast2.right.value == "department == 'Marketing'"


# Test Case 2: 
# Combine Rules and Verify Combined AST
# Objective: Combine two rules and ensure the combined AST reflects correct logical structure.
# Input: List of rule strings.
# Expected Output: AST with combined logic (using AND/OR operators).

def test_combine_rules():
    # Rule 1
    rule1 = "age > 30 AND department = 'Sales'"
    ast1 = parse_rule_to_ast(rule1)
    
    # Rule 2
    rule2 = "age < 25 AND department = 'Marketing'"
    ast2 = parse_rule_to_ast(rule2)
    
    # Combine Rules
    combined_ast = combine_asts([ast1, ast2])
    
    # Check Combined AST Structure
    assert combined_ast.node_type == "operator"
    assert combined_ast.value == "OR"  # Assuming we combine with OR
    assert combined_ast.left == ast1
    assert combined_ast.right == ast2

# Test Case 3: Evaluate Rule for Different User Data
# Objective: Verify that the evaluate_rule function correctly evaluates eligibility based on the rule and user attributes.
# Input: Rule AST and user data (JSON).
# Expected Output: Boolean indicating whether the user meets the rule criteria.

def test_evaluate_rule():
    # Rule: age > 30 AND department = 'Sales'
    rule_ast = parse_rule_to_ast("age > 30 AND department = 'Sales'")
    
    # User Data
    user1 = {"age": 35, "department": "Sales"}
    user2 = {"age": 25, "department": "Marketing"}
    
    # Evaluation
    assert evaluate_ast(rule_ast, user1) == True  # Should pass
    assert evaluate_ast(rule_ast, user2) == False  # Should fail

# Test Case 4: Additional Rules Combination
# Objective: Test combining more complex rules and verifying their evaluation.
# Input: Multiple rules, more complex than previous examples.
# Expected Output: Correct combined AST and accurate evaluation for various user data.

def test_combine_complex_rules():
    # Complex Rule 1
    rule1 = "age > 30 AND department = 'Sales'"
    
    # Complex Rule 2
    rule2 = "(salary > 50000 OR experience > 5)"
    
    # Combine the two rules
    combined_ast = combine_asts([parse_rule_to_ast(rule1), parse_rule_to_ast(rule2)])
    
    # User Data
    user1 = {"age": 40, "department": "Sales", "salary": 60000, "experience": 3}
    user2 = {"age": 28, "department": "Marketing", "salary": 45000, "experience": 6}
    
    # Evaluate Combined Rule
    assert evaluate_ast(combined_ast, user1) == True
    assert evaluate_ast(combined_ast, user2) == False  # Should fail due to department