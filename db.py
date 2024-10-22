# Database Layer
# Database Design (PostgreSQL Example):

# Table: rules
# id (Primary Key)
# rule_name (String)
# ast_structure (JSON)
# created_at (Timestamp)

CREATE TABLE rules (
    id SERIAL PRIMARY KEY,
    rule_name VARCHAR(255),
    ast_structure JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

# Sample Entry for a Rule:


# {
    # "rule_name": "rule1",
    # "ast_structure": {
        # "type": "operator",
        # "value": "AND",
        # "left": {
            # "type": "operator",
            # "value": "OR",
            # "left": {
                # "type": "operand",
                # "value": "age > 30 AND department = 'Sales'"
            # },
            # "right": {
                # "type": "operand",
                # "value": "age < 25 AND department = 'Marketing'"
            # }
        # },
        # "right": {
            # "type": "operator",
            # "value": "OR",
            # "left": {
                # "type": "operand",
                # "value": "salary > 50000"
            # },
            # "right": {
                # "type": "operand",
                # "value": "experience > 5"
            # }
        # }
    # }
# }