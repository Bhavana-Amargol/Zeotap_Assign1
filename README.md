# Zeotap_Work1

# Rule Engine Application

This project is a simple 3-tier rule engine to evaluate user eligibility based on attributes like age, department, income, and spend.

## Application Structure
- **Frontend**: Built using HTML/CSS/JavaScript for rule creation, modification, and evaluation.
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
   git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git

   
