# Python Project Modules

This project contains various Python modules demonstrating different programming concepts and functionalities.

## Project Structure

```
.
├── calculator/
│   ├── __init__.py
│   ├── basic_calculator.py
│   └── scientific_calculator.py
├── library/
│   ├── __init__.py
│   ├── book_management.py
│   ├── user_management.py
│   └── loan_management.py
├── tests/
│   ├── test_calculator.py
│   └── test_mongodb.py
├── mongodb_operations.py
├── requirements.txt
└── README.md
```

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Calculator Module

The calculator module provides basic and scientific calculator functionalities.

### Basic Calculator
```python
from calculator import BasicCalculator

calc = BasicCalculator()
result = calc.add(5, 3)  # 8
result = calc.multiply(4, 2)  # 8
```

### Scientific Calculator
```python
from calculator import ScientificCalculator

calc = ScientificCalculator()
result = calc.sin(0)  # 0
result = calc.factorial(5)  # 120
```

## Library Management System

The library module implements a simple library management system with book, user, and loan management.

### Book Management
```python
from library import Book, Library

library = Library()
book = Book(1, "Python Programming", "John Doe", "123-456")
library.add_book(book)
```

### User Management
```python
from library import User, UserManager

user_manager = UserManager()
user = User(1, "Alice", "alice@email.com", "123-456-7890")
user_manager.add_user(user)
```

### Loan Management
```python
from library import Loan, LoanManager

loan_manager = LoanManager(library, user_manager)
loan = loan_manager.create_loan(book.book_id, user.user_id)
```

## MongoDB Operations

The MongoDB operations module provides a wrapper for common MongoDB operations.

```python
from mongodb_operations import MongoDBOperations

mongo_ops = MongoDBOperations()
doc_id = mongo_ops.insert_single_document({"name": "John", "age": 30})
```

## Running Tests

Run all tests:
```bash
python -m pytest tests/
```

Run tests with coverage report:
```bash
python -m pytest tests/ --cov=.
```

## Features

### Calculator Module
- Basic arithmetic operations
- Scientific calculations
- Error handling
- Static methods for easy use

### Library Management System
- Book management (add, remove, find)
- User management (add, remove, find)
- Loan management (create, return, find)
- Status tracking

### MongoDB Operations
- CRUD operations
- Query operations
- Aggregation
- Indexing
- Pagination

## Requirements

- Python 3.8+
- MongoDB 4.4+
- Dependencies listed in requirements.txt

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 