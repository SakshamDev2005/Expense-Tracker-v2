# Expense-Tracker-v2


# Overview
This revised Expense Tracker program is a simple command-line application designed to help users manage and track their expenses. With simple modifications and integration of AI model, it gives user more facilitation in managing and tracking expenses. 

# Features
1. Show Table: Display a table of recorded expenses.
2. Make an Entry: Add a new transaction with details including date, description, and amount.
3. Sum of Transactions: Calculate and display the total expenses within a specified date range.
4. AI Assistant: Ask questions about the expense data and receive AI-generated responses.
5. Exit System: Safely exit the application.

# Requirements
To run this application, ensure you have the following Python libraries installed:

- pandas
- langchain-anthropic
- langchain-core
- langchain-community

You can install the required libraries using pip:
```
pip install pandas langchain-anthropic langchain-core langchain-community

```

# File Structure
- exp_page.csv: A CSV file that holds the expense records with headers: Date, Transaction, and Amount.

- expense_tracker.py: The main script where the Exp_Tracker class is defined, implementing the core functionality of the application.

# Example Usage
1. Show Table: Display current expenses.
2. Make an Entry: Input transaction details.
3. Sum of Transactions: Specify a date range and get the total amount.
4. Ask AI Assistant: Inquire about your expenses in natural language.
