Grocery Store Inventory Management System

Introduction

The Grocery Store Inventory Management System is a Python-based desktop application designed to simplify grocery store billing and basic sales management. It uses Tkinter for the graphical user interface and MySQL for database management.
The application provides login and signup functionality for employees and store managers. Employees can generate bills by selecting grocery items and entering quantities, while store managers can view sales records.

Features

Login and Signup: Allows employees and store managers to access the application.

User Management: Stores usernames, passwords, names, phone numbers, and designations.

Interactive GUI: Provides a user-friendly interface using Tkinter.

Item Selection: Allows users to select grocery items from a dropdown menu or enter item codes.

Automated Billing: Calculates item prices and the total bill amount.

Bill Management: Supports adding and deleting items before generating a bill.

Sales Records: Stores the total quantity sold and total cost of each bill in the database.

Sales Viewing: Allows store managers to view sales records.

Technologies Used

Front End

Python
Tkinter

Back End

MySQL
mysql.connector

Development Environment

Python IDLE
MySQL Shell
Windows 11

Project Structure

Grocery-Store-Inventory-Management/
│
├── main.py          # Login, signup, and sales page
├── billpage.py      # Billing system
└── README.md        # Project documentation

Note: Rename the Python files in this structure to match the actual filenames in your project.

Database Structure

The application uses a MySQL database named grocery_store.

The main tables used are:
user_info: Stores user credentials, personal details, and designations.
items: Stores item codes, names, and prices.
sales: Stores the total quantity and total cost of generated bills.

Requirements

Python 3.x
MySQL Server

Tkinter

mysql-connector-python
