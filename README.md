# Zeotap_Work1

# Rule Engine Application

This project is a simple 3-tier rule engine to evaluate user eligibility based on attributes like age, department, income, and spend.

## Application Structure
**Frontend**: Built using HTML/CSS/JavaScript for rule creation, modification, and evaluation.
A simple web interface built using HTML/CSS and JavaScript (React.js or vanilla JS).
The UI will allow users to:
Create new rules.
View existing rules.
Modify rules.
Run eligibility checks for user input data.

**API**: Built using Flask, handling rule parsing (AST), combination, and evaluation.
A Python-based REST API using Flask or FastAPI.
API endpoints to handle rule creation, combination, and evaluation.

**Database**: PostgreSQL for storing ASTs and rule metadata.
A PostgreSQL or MongoDB database to store rules and metadata.
The database will store rules in AST format for efficient querying and updates.

## Running the Application

1. Clone the repository:
   ```bash
   git clone https://github.com/Bhavana-Amargol/Zeotap_App1.git

 ## API Endpoints
2. Create Rule: /create_rule - Accepts a rule string and stores it in the database.
3. Combine Rules: /combine_rules - Combines multiple rules into a single AST.
4. Evaluate Rule: /evaluate_rule - Evaluates a rule AST against user attributes.

## Preferred Versions
5. Flask==2.1.1
6. ast==0.0.2
7. psycopg2==2.9.1  # if using PostgreSQL

## To test
```bash
pip install pytest
pytest testcase.py
```

# Bonus Features
1. Error Handling for Invalid Rules
Objective: Implemented error handling for incorrect rule strings (syntax errors, invalid operators, etc.) and data formats.
2. Attribute Catalog Validation
Objective: Ensured that attributes like age, department, salary, etc., are part of a predefined catalog. Invalid attributes should raise an error.
3. Rule Modification Functionality
Objective: Allows modification of existing rules to change operators, operand values, or add/remove sub-expressions.

   
