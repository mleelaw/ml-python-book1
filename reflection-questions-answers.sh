```bash
# Python and SQL Review Questions and Answers

## if Statements

### Q1: Do I understand how to use elif and else in conjunction with if?
# ANSWER:
# In Python, if, elif, and else statements allow us to create conditional logic flows.
# The if statement checks the first condition. If it evaluates to True, that code block executes and the rest are skipped.
# elif (short for 'else if') provides additional conditions to check, but only if all previous conditions were False. These conditions are mutually exclusive - only one block will execute.
# else is a catch-all that executes when all if and elif conditions are False. It doesn't have a condition.
#
# Example:
# if request_method == "GET":
#     # handle GET request
# elif request_method == "POST":
#     # handle POST request  
# elif request_method == "DELETE":
#     # handle DELETE request
# else:
#     # return 405 Method Not Allowed
#
# The key point is that elif creates a chain of mutually exclusive conditions, while multiple if statements would check each condition independently.

### Q2: What is the difference between using == and is / is not with an if statement?
# ANSWER:
# == checks for value equality - it compares whether two objects have the same value or content.
# is checks for identity equality - it compares whether two variables refer to the exact same object in memory.
#
# Example:
# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# list3 = list1
#
# list1 == list2  # True - same values
# list1 is list2  # False - different objects in memory
# list1 is list3  # True - same object in memory
#
# Best practices:
# - Use == for comparing values, which is most common
# - Use is primarily for:
#   - Checking against None: if x is None:
#   - Checking boolean values: if x is True:
#   - Checking against singleton objects

### Q3: How would I check to see if a dictionary had a key with an if statement?
# ANSWER:
# There are several ways to check if a dictionary has a key:
#
# 1. Using the in operator:
# if "price" in order:
#     # use order["price"]
#
# 2. Using .get() with a default:
# if order.get("price") is not None:
#     # key exists
#
# 3. Using .keys():
# if "price" in order.keys():
#     # key exists
#
# The most Pythonic approach is using in directly on the dictionary. It's clean, readable, and efficient.

## for Loops

### Q1: Write a for loop to iterate over elements in a list or tuple?
# ANSWER:
# Basic syntax for iterating over a list:
# my_list = [1, 2, 3, 4, 5]
# for item in my_list:
#     print(item)
#
# For a tuple:
# ports = ("antwerp", "shanghai", "los angeles")
# for port in ports:
#     print(port)
#
# The syntax is the same for both lists and tuples.

## Functions

### Q1: Write the code that defines and calls a simple function in Python?
# ANSWER:
# # Define the function
# def greet(name):
#     return f"Hello, {name}!"
#
# # Call the function
# message = greet("John")
# print(message)  # Output: Hello, John!

### Q2: Explain the concepts of function arguments and return values?
# ANSWER:
# Arguments are the actual values you pass into a function when calling it.
# Parameters are the variable names in the function definition that receive the arguments.
# Return values are the data that a function sends back to the caller using the return statement.
#
# Example:
# def add_numbers(x, y):  # x and y are parameters
#     return x + y        # return value
#
# result = add_numbers(5, 3)  # 5 and 3 are arguments

### Q3: Describe the technical difference between a method and a function?
# ANSWER:
# A method is a function that belongs to an object/class and is called on an instance.
# A function is standalone, not attached to any object.
#
# Example:
# my_list = [1, 2, 3]
# my_list.append(4)  # Method - called ON the list object
# len(my_list)       # Function - called with the list as argument
#
# Methods are accessed using dot notation on objects, while functions are called independently.

### Q4: What do I need to do to invoke a function that is defined in a different module?
# ANSWER:
# You need to import the function from its module. There are several ways:
#
# # Import specific function
# from orders import list_orders
#
# # Import entire module
# import orders
# # Then use: orders.list_orders()
#
# # Import with alias
# from orders import list_orders as get_all_orders

## Classes

### Q1: What is the purpose of a class in object-oriented programming (OOP)?
# ANSWER:
# Classes serve as blueprints or templates for creating objects. They allow us to:
# 1. Encapsulate related data and behaviors - grouping properties and methods that belong together
# 2. Create reusable code - define once, instantiate many times
# 3. Model real-world concepts - like Orders, Customers, or Ships in our system
# 4. Establish consistent structure - all instances share the same attributes and methods
# 5. Enable inheritance - build new classes based on existing ones

### Q2: How does defining a class differ from instantiating an object of that class?
# ANSWER:
# Defining a class creates the blueprint or template - it specifies what attributes and methods objects of that class will have, but doesn't create any actual objects.
# Instantiating creates an actual object (instance) from that blueprint and typically assigns it to a variable.
#
# Example:
# # Definition - creates the blueprint
# class Ship:
#     def __init__(self, name):
#         self.name = name
#
# # Instantiation - creates actual objects
# titanic = Ship("Titanic")  # Creates instance 1
# voyager = Ship("Voyager")  # Creates instance 2

## Modules

### Q1: Can I explain what a Python module is and why it is useful?
# ANSWER:
# A Python module is a file containing Python code that can be imported and used in other Python files. It's useful because it:
# 1. Organizes code - groups related functions and classes together
# 2. Promotes reusability - write once, import anywhere
# 3. Prevents naming conflicts - creates separate namespaces
# 4. Makes code maintainable - easier to find and update specific functionality

### Q2: Do I know how to import and use functions from a module?
# ANSWER:
# Different ways to import:
# # Import specific functions
# from orders import list_orders, retrieve_order
#
# # Import entire module
# import orders
# # Then use: orders.list_orders()
#
# # Import with alias
# from orders import list_orders as get_all_orders
# import orders as ord

### Q3: What are the benefits of packages when developing Python projects?
# ANSWER:
# Benefits of packages:
# 1. Namespace organization - Avoid naming conflicts between modules
# 2. Logical grouping - Related modules stay together (views/, models/, etc.)
# 3. Cleaner imports - Can import from package level
# 4. Hierarchical structure - Can have sub-packages
# 5. Import control - __init__.py manages what's exposed
# 6. Prevents circular imports - Better dependency management

## HTTP Response Codes

### Q1: When a server throws an unexpected exception, which status code should I send to the client in the response?
# ANSWER: 500 Internal Server Error

### Q2: If the client requested a supported resource that doesn't exist, what status code should be part of the response meta-data?
# ANSWER: 404 Not Found

### Q3: If the client did not send all of the required data in the payload of the request, what status code should be part of the response meta-data?
# ANSWER: 400 Bad Request

### Q4: If the client tries to perform an action (GET, POST, PUT, or DELETE) that isn't supported by the API, what status code should be part of the response meta-data?
# ANSWER: 405 Method Not Allowed

## Data Structures

### Q1: Where do I create, modify, and access elements in a Python list?
# ANSWER:
# Creating a list:
# my_list = []  # Empty list
# ships = ["titanic", "voyager", "enterprise"]  # List with values
#
# Adding elements:
# ships.append("discovery")  # Add to end
# ships.insert(0, "mayflower")  # Insert at specific position
# ships.extend(["columbia", "challenger"])  # Add multiple items
#
# Modifying elements:
# ships[0] = "new_ship"  # Change existing element
#
# Accessing elements:
# first_ship = ships[0]  # Get by index
# last_ship = ships[-1]  # Last element
# first_two = ships[0:2]  # Slicing

### Q2: If I was asked in an interview to describe a dictionary, what would I say?
# ANSWER:
# A Python dictionary is a mutable, unordered collection of key-value pairs. Each key must be unique and immutable (like strings, numbers, or tuples), while values can be any data type. Dictionaries provide fast lookups by key, making them ideal for mapping relationships.
#
# Key features:
# - Mutable (can be modified after creation)
# - Keys must be unique
# - Very fast key-based access (O(1) average)
# - Unordered (before Python 3.7) or insertion-ordered (3.7+)

### Q3: Explain how to access and modify values based on keys in a dictionary.
# ANSWER:
# Accessing values:
# order = {"id": 1, "customer": "John", "total": 25.99}
# id_value = order["id"]  # Using square brackets
# customer = order.get("customer")  # Using .get() method
#
# Modifying values:
# order["total"] = 30.99  # Change existing value
# order["status"] = "pending"  # Add new key-value pair
# order.update({"total": 35.99, "items": 3})  # Update multiple

### Q4: Explain the difference between an object and a dictionary in Python.
# ANSWER:
# Main differences:
# 1. Objects have methods (functions) while dictionaries only store data
# 2. Objects use dot notation for access (obj.property)
# 3. Objects are created from classes
# 4. Dictionaries use bracket notation (dict["key"])
# 5. Dictionaries are just data containers

### Q5: What can an object do that a dictionary can't?
# ANSWER:
# Objects can have methods (behaviors), while dictionaries only store data.
# Example:
# class Order:
#     def calculate_tax(self):
#         return self.total * 0.08
#
# Objects encapsulate both data and the behaviors that operate on that data.

## Try/Except

### Q1: Explain the purpose of a try/except block in Python?
# ANSWER:
# Try/except is for error handling:
# - try: Attempt to run code that might fail
# - except: Run this code IF an error occurs in the try block
#
# The purpose is to:
# 1. Gracefully handle errors instead of crashing
# 2. Provide fallback behavior when things go wrong
# 3. Give useful error messages to users
# 4. Prevent program termination from exceptions

## SQL

### Q1: Explain what SQL is and why it is used in software development.
# ANSWER:
# SQL (Structured Query Language) is a standardized language used to communicate with relational databases. It allows developers to:
# 1. Create and modify database structures (tables, relationships)
# 2. Query data - retrieve specific information
# 3. Insert, update, and delete records
# 4. Manage relationships between data
#
# We use SQL because it provides a consistent, powerful way to work with structured data across different database systems.

### Q2: Write a basic SQL query to select a single record from the ReceiptItem database table.
# ANSWER:
# SELECT * FROM ReceiptItem
# WHERE id = 1

### Q3: Construct a SQL query that returns all receipt items, but includes the product name and the receipt total amount?
# ANSWER:
# SELECT 
#     ri.id, 
#     ri.quantity, 
#     ri.line_total,
#     p.name AS product_name,
#     r.total_amount AS receipt_total
# FROM ReceiptItem ri
# JOIN Product p ON ri.product_id = p.id
# JOIN Receipt r ON ri.receipt_id = r.id

### Q4: Demonstrate using the WHERE clause to filter records in a SQL query that returns all receipts with a total that is greater than 100.00.
# ANSWER:
# SELECT * FROM Receipt 
# WHERE total_amount > 100.00

### Q5: Update your previous query to exclude receipts that were generated before 2024.
# ANSWER:
# SELECT * FROM Receipt 
# WHERE total_amount > 100.00 
# AND date >= '2024-01-01'
```